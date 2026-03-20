# ds\_grid\_get\_disk\_max

This function can be used to find the maximum value for all the cells found within the defined disk area of a grid, as shown in the image below:

#### Syntax:

ds\_grid\_get\_disk\_max(index, xm, ym, r)

| Argument | Type | Description |
| --- | --- | --- |
| index |  | The handle of the grid. |
| xm |  | The x position of the disk center in the grid. |
| ym |  | The y position of the disk center in the grid. |
| r |  | The radius of the disk in the grid. |

 

#### Returns:

Real or String

 

#### Example:

val \= ds\_grid\_get\_disk\_max(grid, 5, 5, 2\)

The above code will set the variable "val" to the maximum value contained within the given disk of the DS grid indexed in the variable "grid".
