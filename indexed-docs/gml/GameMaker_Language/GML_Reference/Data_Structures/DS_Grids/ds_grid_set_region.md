# ds\_grid\_set\_region

This function can be used to set a rectangular region of a given grid to a specified value (which can be either a real or a string) as illustrated by the image shown below:

 

#### Syntax:

ds\_grid\_set\_region(index, x1, y1, x2, y2, val)

| Argument | Type | Description |
| --- | --- | --- |
| index |  | The handle of the grid. |
| x1 |  | The x position of the left of the region in the grid. |
| y1 |  | The y position of the top of the region in the grid. |
| x2 |  | The x position of the right of the region in the grid. |
| y2 |  | The y position of the bottom of the region in the grid. |
| val |  | The value to set the region cells to. |

 

#### Returns:

 

#### Example:

ds\_grid\_set\_region(grid, 5, 5, 10, 10, 99\)

This would set all cells within the region of the grid indexed in the variable "grid" from (5,5\) to (10,10\) to 99\.
