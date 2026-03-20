# draw\_surface\_stretched\_ext

This function does exactly the same as the [draw\_surface\_stretched](draw_surface_stretched.md) function with the added ability to set the colour blending and alpha value for the surface when it is drawn (similar to the function [draw\_surface\_ext](draw_surface_ext.md)).

 
 

#### Syntax:

draw\_surface\_stretched\_ext(surface, x, y, w, h, col, alpha)

| Argument | Type | Description |
| --- | --- | --- |
| surface | [Surface](surface_create.md) | The surface to draw. |
| x | [Real](../../../GML_Overview/Data_Types.md) | The x position of where to draw the surface. |
| y | [Real](../../../GML_Overview/Data_Types.md) | The y position of where to draw the surface. |
| w | [Real](../../../GML_Overview/Data_Types.md) | The width at which to draw the surface. |
| h | [Real](../../../GML_Overview/Data_Types.md) | The height at which to draw the surface. |
| colour | [Colour](../Colour_And_Alpha/Colour_And_Alpha.md) | The colour with which to colour the surface. |
| alpha | [Real](../../../GML_Overview/Data_Types.md) | The alpha with which to blend the surface. |

 

#### Returns:

N/A

 

#### Example:

draw\_surface\_stretched\_ext(surf, x, y, 200, 200, c\_white, 0\.5\);

This will draw the given surface with its top\-left corner at the instance's (x, y) position, stretched to occupy an area of 200x200 pixels, with no blending but partially transparent.
