# ds\_grid\_set\_disk

With this function you can set a circular region of a grid to a certain value. You need to supply a starting grid cell (as an x and y axis coordinate) as well as the radius of the disk to set and the value that you wish to set the disk too, as shown by the illustration below:

 

#### Syntax:

ds\_grid\_set\_disk(index, xm, ym, r, val)

| Argument | Type | Description |
| --- | --- | --- |
| index |  | The handle of the grid. |
| xm |  | The x position of the disk on the grid. |
| ym |  | The y position of the disk on the grid. |
| r |  | The radius of the disk on the grid. |
| val |  | The value to set with the cells within the disk. |

 

#### Returns:

 

#### Example:

ds\_grid\_set\_disk(grid, ds\_grid\_width(grid) div 2, ds\_grid\_height(grid) div 2, 5, \-4\)

The above code will set a circular region with a radius of 5 cells in the DS grid indexed in the variable "grid" to a value of \-4\.
