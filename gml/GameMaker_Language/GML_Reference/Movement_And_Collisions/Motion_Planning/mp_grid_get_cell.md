# mp\_grid\_get\_cell

This function returns whether the given MP grid cell is flagged as occupied or not. If it has been occupied or the position being checked is out of the grid's bounds, the function will return \-1, otherwise it will return 0\.

 

#### Syntax:

mp\_grid\_get\_cell(id, x , y)

| Argument | Type | Description |
| --- | --- | --- |
| id | [MP Grid ID](mp_grid_create.md) | Index of the mp\_grid that is to be used |
| x1 | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate of the grid to check |
| y1 | [Real](../../../GML_Overview/Data_Types.md) | The y coordinate of the grid to check |

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

if (mp\_grid\_get\_cell(grid, mouse\_x div 16, mouse\_y div 16\) \=\= \-1\)  

 {  

     image\_blend \= c\_red;  

 }  

 else  

 {  

     image\_blend \= c\_lime;  

 }

The above code will check the mp\_grid cell that corresponds to the mouse position and, if it is occupied, sets the [image\_blend](../../Asset_Management/Sprites/Sprite_Instance_Variables/image_blend.md) variable to red, and if it is not occupied it sets it to green.
