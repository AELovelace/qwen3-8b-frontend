# ds\_grid\_add\_region

This function can be used to add a given value (real or string) to all the values of the cells found within the defined area of a grid. The value to be added must be of the same type as that held within the grid cells, ie: you cannot add a string to a real or vice versa, and for strings this corresponds to concatenation.

 

#### Syntax:

ds\_grid\_add\_region(index, x1, y1, x2, y2, val)

| Argument | Type | Description |
| --- | --- | --- |
| index | [DS Grid](ds_grid_create.md) | The handle of the grid. |
| x1 | [Real](../../../GML_Overview/Data_Types.md) | The x position of the left of the region in the grid. |
| y1 | [Real](../../../GML_Overview/Data_Types.md) | The y position of the top of the region in the grid. |
| x2 | [Real](../../../GML_Overview/Data_Types.md) | The x position of the right of the region in the grid. |
| y2 | [Real](../../../GML_Overview/Data_Types.md) | The y position of the bottom of the region in the grid. |
| val | [Any](../../../GML_Overview/Data_Types.md#variable) | The value to add to the region cells. |

 

#### Returns:

N/A

 

#### Example:

ds\_grid\_add\_region(grid, 2, 4, 5, 5, ".")

This would add "." to all the strings held in the cells within the defined region of the DS grid referenced by the variable "grid".
