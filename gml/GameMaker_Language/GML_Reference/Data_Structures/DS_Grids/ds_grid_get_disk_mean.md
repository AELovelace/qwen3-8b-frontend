# ds\_grid\_get\_disk\_mean

This function can be used to find the mean value for all the cells found within the defined disk area of a grid (all cell values are added together and then divided by the total number of cells that make up the disk), as shown in the image below:

 

#### Syntax:

ds\_grid\_get\_disk\_mean(index, xm, ym, r)

| Argument | Type | Description |
| --- | --- | --- |
| index |  | The handle of the grid. |
| xm |  | The x position of the disk on the grid. |
| ym |  | The y position of the disk on the grid. |
| r |  | The radius of the disk on the grid. |

 

#### Returns:

Real or String

 

#### Example:

val \= ds\_grid\_get\_disk\_mean(grid, 5, 5, 2\)

The above code will set the variable "val" to the mean value contained within the given disk of the DS grid indexed in the variable "grid".
