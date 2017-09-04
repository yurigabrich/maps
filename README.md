# Useful tools

- `geo_conversor.py`

     Based on a external text file comprised with particular inputs, the software remove boundaries between specified areas. For example:
     1. Each geographic coordinate area must be formatted in 3 paragraphs. The first paragraph is the name of the respective coordinate area, the second, the coordinate numbers themselves and then followed by an empty paragraph. This pattern is used to get the values correctly and its setted in variable `size`, inside function `load_geo`. Note that coordinate numbers must be written in the format of latitude, longitude and elevation (used here as x,y,z) and each set of coordinate separated by a space.
     
     **Inside text file named _coord.txt_**
     ```
     Area 1:
     x1,y1,z1 x2,y2,z2 x3,y3,z3 x4,y4,z4, x5,y5,z5
     
     Area 2:
     x6,y6,z6 x7,y7,z7 x3,y3,z3 x4,y4,z4, x8,y8,z8
     
     ```
     
     2. Call function `workDONE` to get a new coordinate area. Note that file _coord.txt_ will get a new set of coordinates named accordingly with `for` loop iteration number.
     
     **Prompt command**
     ```
     workDONE('coord.txt','Area 1:','Area 2:')
     ```
     
     **Inside text file named _coord.txt_**
     ```
     Area 1:
     x1,y1,z1 x2,y2,z2 x3,y3,z3 x4,y4,z4, x5,y5,z5
     
     Area 2:
     x6,y6,z6 x7,y7,z7 x3,y3,z3 x4,y4,z4, x8,y8,z8
     
     1:
     x1,y1,z1 x2,y2,z2 x7,y7,z7 x6,y6,z6 x8,y8,z8 x5,y5,z5
     ```
