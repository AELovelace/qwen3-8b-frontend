# ds\_grid\_create

This function creates a new DS grid data structure of the specified cell width and height. The function returns [DS Grid](ds_grid_create.md) [Handle](../../../GML_Overview/Data_Types.md) which must be used in all further functions that deal with this DS grid.

 

#### Syntax:

ds\_grid\_create(w, h)

| Argument | Type | Description |
| --- | --- | --- |
| w | [Real](../../../GML_Overview/Data_Types.md) | The width of the grid to be created. |
| h | [Real](../../../GML_Overview/Data_Types.md) | The height of the grid to be created. |

 

#### Returns:

[DS Grid](ds_grid_create.md)

 

#### Example:

mygrid \= ds\_grid\_create(10, 10\);

This creates a grid 10 cells high and 10 cells wide.
