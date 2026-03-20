# draw\_surface

This function draws a surface at a given position within the room, with the top left corner of the surface being drawn at the specified x/y position.

 
 

#### Syntax:

draw\_surface(id, x, y)

| Argument | Type | Description |
| --- | --- | --- |
| id | [Surface](surface_create.md) | The surface to draw. |
| x | [Real](../../../GML_Overview/Data_Types.md) | The x position of where to draw the surface. |
| y | [Real](../../../GML_Overview/Data_Types.md) | The y position of where to draw the surface. |

 

#### Returns:

N/A

 

#### Example:

var \_vx \= camera\_get\_view\_x(view\_camera\[0]);  

 var \_vy \= camera\_get\_view\_y(view\_camera\[0]);  

draw\_surface(surf, \_vx, \_vy);
 

The above code draws the surface indexed in surf at same position as camera view\[0].
