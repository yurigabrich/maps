def load_geo(file_name, count=0):
    '''
    file_name (string): the name of the file containing the list of string elements to load.
    
    Returns: a list of strings bundled as a combination of name of the state, geolocations and a null paragraph.
    
    Depending on the size of the input file, this function may take a while to finish.
    ''' 
    if count == 0:
        print('\n''Loading coordinates from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    
    # geolocations: LIST of STRINGS
    geolocations = in_file.readlines() # line delimiter \n
    in_file.close()
    
    # ignoring past simulated values
    if (count == 0) and ('1:\n' in geolocations):
        pos_1 = geolocations.index('1:\n')
        geolocations = geolocations[:pos_1]

        # deleting past values
        re = open(file_name,'w')
        for line in geolocations:
            re.write(line)
        re.close()

    size = int(len(geolocations)/3) 

    if count == 0:
        message = '\n Geolocations loaded successfully with ' + str(size) + ' data entries.'
    else:
        message = 4*'\t' +'   ... ' + str(size) + ' ...'

    # end of load_geo, if everything is right
    print(message)
    return geolocations


def catalog(geolocations):
	'''
	Converts the input file to dictionary format.
	'''
	GeoByState = {}

	for i in range( 0 , len(geolocations) , 3 ):
		GeoByState[geolocations[i][:-1]] = geolocations[i+1][:-1]

	return GeoByState


def invert(string):
    '''
    Inverts the direction of 'reading' a string.
    '''
    inverted = ''
    for element in string.split(' '):
        inverted = element + ' ' + inverted
    
    return inverted


def boundless(refGeo, compGeo):
    '''
	Concatenates both input as one geo coordination.
    Looks for duplicates and remove it.
    '''
    try:
        firstDuplication = 0
        for coord in compGeo.split(' '):
            if coord in refGeo:                
                # save beginning of border
                if firstDuplication == 0:
                    firstDuplication += 1
                    before = compGeo.find(coord) + len(coord) + 1
                    first = refGeo.find(coord) + len(coord) + 1
                    
                # update the last one of the edge
                after = compGeo.find(coord) + len(coord) + 1
                last = refGeo.find(coord) + len(coord) + 1
            
            else:
                # after define the edges
                if firstDuplication != 0:
                    # remove borders from compGeo
                    compGeoB = invert(compGeo[ 0 : before ])
                    compGeoA = invert(compGeo[ after : ])
                                      
                    # remove borders from refGeo
                    if last < first:
                        refGeoB = refGeo[ 0 : last ]
                        refGeoA = refGeo[ first : ]
                        change = refGeoB
                        refGeoB = invert(refGeoA)
                        refGeoA = invert(change)
                    else:
                        refGeoB = refGeo[ 0 : first ]
                        refGeoA = refGeo[ last : ]
                    
                    break
        
        return refGeoB + compGeoB + compGeoA + refGeoA
    
    except:
        return '\nNo matches between references.'


def workDONE(read_it, x, y):
    '''
    Simple code line to do all hard work. ;)
    '''
    for n in range(len(y)):
        indice = str(n+1) + ':'
        x.append(indice)

        GeoByStates = catalog( load_geo( read_it, n ) )

        refGeo = GeoByStates[x[n]]
        compGeo = GeoByStates[y[n]]
        result = boundless(refGeo, compGeo)

        with open(read_it, 'a') as f: # ATTENTION TO 'a'
            f.write(indice + '\n' + result + '\n\n')

    with open('export.txt', 'w') as f:
        f.write(result)

    return None
