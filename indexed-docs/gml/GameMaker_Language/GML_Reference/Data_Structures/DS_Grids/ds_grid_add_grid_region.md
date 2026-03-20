# ds\_grid\_add\_grid\_region

This function can be used to add all the values of all the cells found within the source area of a grid to the values within the destination grid, as illustrated below:

  You can also use this function on the same grid to add values from one region of the grid to those stored in another (see code example below).

 

#### Syntax:

ds\_grid\_add\_grid\_region(index, source, x1, y1, x2, y2, xpos, ypos)

| Argument | Type | Description |
| --- | --- | --- |
| index | [DS Grid](ds_grid_create.md) | The handle of the destination grid. |
| source | [DS Grid](ds_grid_create.md) | The handle of the source grid. |
| x1 | [Real](../../../GML_Overview/Data_Types.md) | The left position of the region of cells to copy from the source grid. |
| y1 | [Real](../../../GML_Overview/Data_Types.md) | The top position of the region of cells to copy from the source grid. |
| x2 | [Real](../../../GML_Overview/Data_Types.md) | The right position of the region of cells to copy from the source grid. |
| y2 | [Real](../../../GML_Overview/Data_Types.md) | The bottom position of the region of cells to copy from the source grid. |
| xpos | [Real](../../../GML_Overview/Data_Types.md) | The x position on the destination grid to add the source region to. |
| ypos | [Real](../../../GML_Overview/Data_Types.md) | The y position on the destination grid to add the source region to. |

 

#### Returns:

N/A

 

#### Example:

ds\_grid\_add\_grid\_region(grid, grid, 0, 0, 1, 5, 2, 0\);

The above code would copy the region of cells from (0, 0\) to (1, 5\) of the DS grid indexed in the variable grid and add them to the cells from position (2, 0\) of the same DS grid .
