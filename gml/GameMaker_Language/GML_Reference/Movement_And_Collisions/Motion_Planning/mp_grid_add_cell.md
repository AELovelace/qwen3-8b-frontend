# mp\_grid\_add\_cell

This function marks an individual cell within the given MP grid as "forbidden" meaning that the path finding functions will not ever cross it. Now, normally you work in x/y *room* coordinates, and not in MP grid *cell* coordinates. So let's consider the following image which shows how the two can correlate:

As you can see the mp\_grid is numbered as a series of cells (starting at 0,0 in the upper left corner), and when you place this grid over the room there is a direct correlation between the room coordinates (which also start at 0,0 in the top left) and the cells within the grid. In the image you can see that an instance at the position 260,130 falls on the grid cell 8,4\. You can calculate mathematically the exact cell that a position lands on easily by either dividing the number by the grid resolution and then rounding down *or*, if you are using power of 2 grid resolutions (like 8, 16, 32 etc...) you can use the [bitwise operators](../../../../Additional_Information/Bitwise_Operators.md). It should be noted that the bitwise operation is faster and the example below shows both methods.

 

#### Syntax:

mp\_grid\_add\_cell(id, h, v)

| Argument | Type | Description |
| --- | --- | --- |
| id | [MP Grid ID](mp_grid_create.md) | Index of the mp\_grid that is to be used |
| h | [Real](../../../GML_Overview/Data_Types.md) | Horizontal position of the cell in the grid |
| v | [Real](../../../GML_Overview/Data_Types.md) | Vertical position of the cell in the grid |

 

#### Returns:

N/A

 

#### Example:

with (obj\_Wall)  

 {  

     mp\_grid\_add\_cell(grid, floor(x / 32\), floor(y / 32\));  

 }  

 with (obj\_Door)  

 {  

     mp\_grid\_add\_cell(grid, x\>\>5, y\>\>5\);  

 }

The above code will make all "obj\_Wall" and all obj\_Door add their equivalent cell positions into the mp\_grid indexed in the variable "grid". In the first part of the example, this is done by taking the x/y coordinates of the object and dividing them by the resolution of the grid (using floor to keep the values as integers), and in the second part (since the grid resolution is a power of 2\) it is done by bit\-shifting the x,y coordinates 5 places to the right.
