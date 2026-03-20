# draw\_surface\_stretched

This function simply takes a surface and stretches it over the given width and height so that it occupies the area. As with [draw\_surface](draw_surface.md) you can specify a surface and then the (x, y) position in the room for the surface to be drawn at and finally a width and a height (which must be pixel values).

 
 

#### Syntax:

draw\_surface\_stretched(surface, x, y, w, h)

| Argument | Type | Description |
| --- | --- | --- |
| surface | [Surface](surface_create.md) | The surface to draw. |
| x | [Real](../../../GML_Overview/Data_Types.md) | The x position of where to draw the surface. |
| y | [Real](../../../GML_Overview/Data_Types.md) | The y position of where to draw the surface. |
| w | [Real](../../../GML_Overview/Data_Types.md) | The width at which to draw the surface. |
| h | [Real](../../../GML_Overview/Data_Types.md) | The height at which to draw the surface. |

 

#### Returns:

N/A

 

#### Example:

draw\_surface\_stretched(surf, 10, 10, 100, 100\);

This will draw the surface indexed in the variable surf with its top\-left corner at (10, 10\). Its width and height are both set to 100, which is how much space it will occupy regardless of the surface's actual width and height.
