# ds\_grid\_value\_disk\_exists

With this function you can check to see if a specific value (real or string) is present within a circular area of a given DS grid. If it is present the function will return true otherwise it will return false.

 

#### Syntax:

ds\_grid\_value\_disk\_exists(index, xm, ym, r, val)

| Argument | Type | Description |
| --- | --- | --- |
| index | [DS Grid](ds_grid_create.md) | The handle of the grid. |
| xm | [Real](../../../GML_Overview/Data_Types.md) | The x position of the disk on the grid. |
| ym | [Real](../../../GML_Overview/Data_Types.md) | The y position of the disk on the grid. |
| r | [Real](../../../GML_Overview/Data_Types.md) | The radius of the disk on the grid. |
| val | [Any](../../../GML_Overview/Data_Types.md#variable) | The value to find. |

 

#### Returns:

[Boolean](../../../GML_Overview/Data_Types.md)

 

#### Example:

if (ds\_grid\_value\_disk\_exists(grid, 5, 5, 5, val))  

 {  

     xpos \= ds\_grid\_value\_disk\_x(grid, 5, 5, 5, val);  

     ypos \= ds\_grid\_value\_disk\_y(grid, 5, 5, 5, val);  

 }

The above code checks a DS grid for a specific value within a disk region. if it is found, it then stores the x and y position of the value in two variables for later use.
