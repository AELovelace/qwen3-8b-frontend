# ds\_grid\_get\_disk\_sum

This function can be used to add all the values all the cells found within the defined disk area of a grid together, as shown in the image below:

 

#### Syntax:

ds\_grid\_get\_disk\_sum(index, xm, ym, r)

| Argument | Type | Description |
| --- | --- | --- |
| index |  | The handle of the grid. |
| xm |  | The x position of the disk on the grid. |
| ym |  | The y position of the disk on the grid. |
| r |  | The radius of the disk on the grid. |

 

#### Returns:

Real or String

 

#### Example:

val \= ds\_grid\_get\_disk\_sum(grid, 5, 5, 2\)

The above code will set the variable "val" to the sum of all values contained within the given disk of the DS grid indexed in the variable "grid".
