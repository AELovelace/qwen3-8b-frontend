# ds\_grid\_set

This function can be used to set a given cell within the given DS grid to any value, which can be a real number or a string. The image below illustrates this:

#### Syntax:

ds\_grid\_set(index, x, y, value)

| Argument | Type | Description |
| --- | --- | --- |
| index | [DS Grid](ds_grid_create.md) | This handle of the grid. |
| x | [Real](../../../GML_Overview/Data_Types.md) | The x position of the cell to set. |
| y | [Real](../../../GML_Overview/Data_Types.md) | The y position of the cell to set. |
| value | [Any](../../../GML_Overview/Data_Types.md#variable) | The value with which to set the cell. |

 

#### Returns:

N/A

 

#### Example:

grid \= ds\_grid\_create(5, 5\);  

 var i \= 0;  

 var j \= 0;  

  

 repeat (ds\_grid\_width(grid))  

 {  

     repeat (ds\_grid\_height(grid))  

     {  

         ds\_grid\_set(grid, i, j, irandom(9\));  

         j \+\= 1;  

     }  

       

     j \= 0;  

     i \+\= 1;  

 }
 

The above code creates a grid and stores its index in the variable "grid". It then populates this grid with random integers from 0 to 9\.
