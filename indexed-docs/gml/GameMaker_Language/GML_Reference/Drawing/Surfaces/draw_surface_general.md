# draw\_surface\_general

This function combines the function [draw\_surface\_ext](draw_surface_ext.md) with the function [draw\_surface\_part](draw_surface_part.md), adding in some additional blending options so that each corner of the final surface part can be blended with an individual colour.

  Gradient blending is not available for the HTML5 target unless [WebGL](../../../../Settings/Game_Options/HTML5.md#webgl) is enabled.

 
 

#### Syntax:

draw\_surface\_general(surface, left, top, w, h, x, y, xscale, yscale, rot, c1, c2, c3, c4, alpha)

| Argument | Type | Description |
| --- | --- | --- |
| surface | [Surface](surface_create.md) | The surface to draw. |
| left | [Real](../../../GML_Overview/Data_Types.md) | The left position in the surface of the part to be drawn. |
| top | [Real](../../../GML_Overview/Data_Types.md) | The top position in the surface of the part to be drawn. |
| w | [Real](../../../GML_Overview/Data_Types.md) | The width of the part to be drawn, from left. |
| h | [Real](../../../GML_Overview/Data_Types.md) | The height of the part to be drawn, from top. |
| x | [Real](../../../GML_Overview/Data_Types.md) | The x position of where to draw the surface. |
| y | [Real](../../../GML_Overview/Data_Types.md) | The y position of where to draw the surface. |
| xscale | [Real](../../../GML_Overview/Data_Types.md) | The horizontal scaling to draw the surface with. |
| yscale | [Real](../../../GML_Overview/Data_Types.md) | The vertical scaling to draw the surface with. |
| rot | [Real](../../../GML_Overview/Data_Types.md) | The rotation or angle to draw the surface with. |
| c1 | [Colour](../Colour_And_Alpha/Colour_And_Alpha.md) | The colour of the top\-left corner of the surface. |
| c2 | [Colour](../Colour_And_Alpha/Colour_And_Alpha.md) | The colour of the top\-right corner of the surface. |
| c3 | [Colour](../Colour_And_Alpha/Colour_And_Alpha.md) | The colour of the bottom\-right corner of the surface. |
| c4 | [Colour](../Colour_And_Alpha/Colour_And_Alpha.md) | The colour of the bottom\-left corner of the surface. |
| alpha | [Real](../../../GML_Overview/Data_Types.md) | The alpha transparency to draw the surface with. |

 

#### Returns:

N/A

 

#### Example:

draw\_surface\_general(surf, 8, 8, 32, 32, x, y, 2, 0\.5, 180, c\_white, c\_white, c\_black, c\_black, 1\);

This will draw a 32x32 pixel area from 8x8 pixels into the surface. It will be stretched to double its usual width but half its usual height. It will be opaque, and upside down. The top area of the surface will be blended white and hence normal, but the bottom area will be black, meaning the surface will go from normal to silhouette downwards in a smooth gradient.
