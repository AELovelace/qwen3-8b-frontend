# draw\_surface\_part\_ext

This function draws a part of the chosen surface at the given position following the same rules as per [draw\_surface\_part](draw_surface_part.md), only now you can scale the part, blend a colour with it, or change its alpha when drawing it to the screen (the same as when drawing a surface with [draw\_surface\_ext](draw_surface_ext.md)).

 
 

#### Syntax:

draw\_surface\_part\_ext(surface, left, top, w, h, x, y, xscale, yscale, colour, alpha)

| Argument | Type | Description |
| --- | --- | --- |
| surface | [Surface](surface_create.md) | The surface to draw. |
| left | [Real](../../../GML_Overview/Data_Types.md) | The left position in the surface of the part to be drawn. |
| top | [Real](../../../GML_Overview/Data_Types.md) | The top position in the surface of the part to be drawn. |
| w | [Real](../../../GML_Overview/Data_Types.md) | The width of the part to be draw, from left. |
| h | [Real](../../../GML_Overview/Data_Types.md) | The height of the part to be drawn, from top. |
| x | [Real](../../../GML_Overview/Data_Types.md) | The x position of where to draw the surface. |
| y | [Real](../../../GML_Overview/Data_Types.md) | The y position of where to draw the surface. |
| xscale | [Real](../../../GML_Overview/Data_Types.md) | The horizontal scaling the part should be drawn with. |
| yscale | [Real](../../../GML_Overview/Data_Types.md) | The vertical scaling the part should be drawn with. |
| colour | [Colour](../Colour_And_Alpha/Colour_And_Alpha.md) | The colour blending the part should be drawn with. |
| alpha | [Real](../../../GML_Overview/Data_Types.md) | The alpha transparency the part should be drawn with. |

 

#### Returns:

N/A

 

#### Example:

draw\_surface\_part\_ext(surf, 8, 8, 32, 32, x, y, 2, 0\.5, c\_black, 1\);

This will draw a 32x32 pixel area from 8x8 pixels into the surface indexed in the variable surf. It will be stretched to double its usual width but half its usual height. It will be opaque and it will be blended with black (turning it into a silhouette).
