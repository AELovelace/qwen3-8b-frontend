# ds\_grid\_get

This function can be used to get the value from any cell within the given DS grid. If you pass invalid grid coordinates to the function, then the value returned will be undefined and an error will be shown in the output window.

 

#### Syntax:

ds\_grid\_get(index, x, y)

| Argument | Type | Description |
| --- | --- | --- |
| index |  | The handle of the grid. |
| x |  | The x position of the cell you want to find the value of. |
| y |  | The y position of the cell you want to find the value of. |

 

#### Returns:

Variable

 

#### Example:

var xx \= irandom(ds\_grid\_width(grid) \- 1\);
   

 var yy \= irandom(ds\_grid\_height(grid) \- 1\);
   

 val \= ds\_grid\_get(grid, xx, yy)

The above code selects a random cell from the DS grid indexed in the variable "grid" and stores its value in the variable "val".
