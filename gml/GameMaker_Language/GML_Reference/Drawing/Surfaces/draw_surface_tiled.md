# draw\_surface\_tiled

This function takes a surface and then repeatedly tiles it across the whole room, starting from the coordinates that you give in the function.

 
 

#### Syntax:

draw\_surface\_tiled(surface, x, y)

| Argument | Type | Description |
| --- | --- | --- |
| surface | [Surface](surface_create.md) | The surface to draw. |
| x | [Real](../../../GML_Overview/Data_Types.md) | The x position of where to draw the surface. |
| y | [Real](../../../GML_Overview/Data_Types.md) | The y position of where to draw the surface. |

 

#### Returns:

N/A

 

#### Example:

draw\_surface\_tiled(surf, x, y);

This will draw the surface indexed in surf at the instance's own x and y position, tiled in every direction in the room.
