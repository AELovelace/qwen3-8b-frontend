# draw\_surface\_ext

This function draws the given surface as in the function [draw\_surface](draw_surface.md), with additional options to change the scale, blending, rotation and alpha of the surface being drawn.

Changing these additional options does *not* modify the resource in any way (only how it is drawn).

 
 

#### Syntax:

draw\_surface\_ext(id, x, y, xscale, yscale, rot, col, alpha)

| Argument | Type | Description |
| --- | --- | --- |
| id | [Surface](surface_create.md) | The surface to draw. |
| x | [Real](../../../GML_Overview/Data_Types.md) | The x position of where to draw the surface. |
| y | [Real](../../../GML_Overview/Data_Types.md) | The y position of where to draw the surface. |
| xscale | [Real](../../../GML_Overview/Data_Types.md) | The horizontal scale. |
| yscale | [Real](../../../GML_Overview/Data_Types.md) | The vertical scale. |
| rot | [Real](../../../GML_Overview/Data_Types.md) | The rotation or angle to draw the surface. |
| col | [Colour](../Colour_And_Alpha/Colour_And_Alpha.md) | The colour with which to blend the surface. |
| alpha | [Real](../../../GML_Overview/Data_Types.md) | The alpha transparency for drawing the surface. |

 

#### Returns:

N/A

 

#### Example:

draw\_surface\_ext(surf, 0, 0, 2, 2, 0, c\_red, 0\.5\);

The above code draws the surface stored in the variable surf at the (0, 0\) position in the room at twice the original scale, blended red and semi transparent.
