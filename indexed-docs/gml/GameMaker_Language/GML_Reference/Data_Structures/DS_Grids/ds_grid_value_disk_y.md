# ds\_grid\_value\_disk\_y

With this function you can get the y coordinate (within the given grid disc\-shaped region) of the value being searched for. You give the DS grid index (as returned by [ds\_grid\_create()](ds_grid_create.md)) along with the x/y positions for the center cell of the disk. Then you give the radius (as an integer value) around the center cell to search, before supplying the value to search for. If the value being searched for does not exist, then the function will return \-1\.

 

#### Syntax:

ds\_grid\_value\_disk\_y(index, xm, ym, r, val)

| Argument | Type | Description |
| --- | --- | --- |
| index | [DS Grid](ds_grid_create.md) | The handle of the grid. |
| xm | [Real](../../../GML_Overview/Data_Types.md) | The x position of the disk on the grid. |
| ym | [Real](../../../GML_Overview/Data_Types.md) | The y position of the disk on the grid. |
| r | [Real](../../../GML_Overview/Data_Types.md) | The radius of the disk on the grid. |
| val | [Any](../../../GML_Overview/Data_Types.md#variable) | The value to find. |

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

if (ds\_grid\_value\_disk\_exists(grid, 5, 5, 5, val))  

 {  

     xpos \= ds\_grid\_value\_disk\_x(grid, 5, 5, 5, val);  

     ypos \= ds\_grid\_value\_disk\_y(grid, 5, 5, 5, val);  

 }

The above code checks a DS grid for a specific value within a disk region. if it is found, it then stores the x and y position of the value in two variables for later use.
