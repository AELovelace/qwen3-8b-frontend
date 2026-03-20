# ds\_grid\_clear

This function can be used to clear a given DS grid to a specific value. All cells within the grid will then contain this value, which can be a real number or a string. The image below illustrates how this works:

 

#### Syntax:

ds\_grid\_clear(index, val)

| Argument | Type | Description |
| --- | --- | --- |
| index |  | This handle of the grid to clear. |
| val |  | The new value for all grid cells. |

 

#### Returns:

 

#### Example:

ds\_grid\_resize(global.Grid, room\_width / 32, room\_height / 32\);
   

 ds\_grid\_clear(global.Grid, \-1\)

The above code will resize the DS grid indexed in the global variable "Grid" and then clear it so that each cell holds the value \-1\.
