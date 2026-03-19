# mp\_grid\_clear\_cell

This function clears a specific "cell" of an MP grid. Cells are *not* calculated as room coordinates, but rather as grid coordinates, where (0, 0\) is the top\-left corner of the grid. This means that to clear a cell at a specific position in the room, we must change the x and y coordinates into cell coordinate dividing them by the resolution of the MP grid. The code example below shows how this works.

 

#### Syntax:

mp\_grid\_clear\_cell(id, h, v)

| Argument | Type | Description |
| --- | --- | --- |
| id | [MP Grid ID](mp_grid_create.md) | Index of the mp\_grid that is to be used |
| h | [Real](../../../GML_Overview/Data_Types.md) | Horizontal position of the cell to clear |
| v | [Real](../../../GML_Overview/Data_Types.md) | Vertical position of the cell to clear |

 

#### Returns:

[Boolean](../../../GML_Overview/Data_Types.md)

 

#### Example:

with (obj\_box)  

 {  

     mp\_grid\_clear\_cell(grid, floor(x / 32\), floor(y /32\));  

     instance\_destroy();  

 }

The above code will make all instances of obj\_box destroy themselves and have them mark the cells they occupied in the mp\_grid indexed in the variable grid as free. In this example, we find the appropriate cell by taking the x/y coordinate of the object and dividing them by the resolution of the grid (using [floor](../../Maths_And_Numbers/Number_Functions/floor.md) to keep the values as integers).
