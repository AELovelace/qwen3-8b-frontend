# draw\_surface\_part

This function draws part of any surface at a given position within the room.

As with [draw\_surface](draw_surface.md) you can specify a surface, but you then need to specify the *relative coordinates* within the surface of an area to select for drawing. This means that a left position of 0 and a top position of 0 would be the top\-left corner of the surface and all further coordinates should be taken from that position.

 
 

#### Syntax:

draw\_surface\_part(surface, left, top, w, h, x, y)

| Argument | Type | Description |
| --- | --- | --- |
| surface | [Surface](surface_create.md) | The surface to draw. |
| left | [Real](../../../GML_Overview/Data_Types.md) | The left position in the surface of the part to be drawn. |
| top | [Real](../../../GML_Overview/Data_Types.md) | The top position in the surface of the part to be drawn. |
| w | [Real](../../../GML_Overview/Data_Types.md) | The width of the part to be drawn, from left. |
| h | [Real](../../../GML_Overview/Data_Types.md) | The height of the part to be drawn, from top. |
| x | [Real](../../../GML_Overview/Data_Types.md) | The x position of where to draw the surface. |
| y | [Real](../../../GML_Overview/Data_Types.md) | The y position of where to draw the surface. |

 

#### Returns:

N/A

 

#### Example:

draw\_surface\_part(surf, 8, 8, 32, 32, x, y);

This will draw a 32x32 area 8px by 8px in from the top\-left of the surface indexed in surf, at the instance's (x, y) position.
