# draw\_surface\_tiled\_ext

This function takes a surface and then repeatedly tiles it across the whole room, starting at the coordinates that you give in the function and with each tile scaled, colour blended and with the alpha that you define (these properties are the same as those used in [draw\_surface\_ext](draw_surface_ext.md)).

 
 

#### Syntax:

draw\_surface\_tiled\_ext(surface, x, y, xscale, yscale, col, alpha)

| Argument | Type | Description |
| --- | --- | --- |
| surface | [Surface](surface_create.md) | The surface to draw. |
| x | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate of where to draw the surface. |
| y | [Real](../../../GML_Overview/Data_Types.md) | The y coordinate of where to draw the surface. |
| xscale | [Real](../../../GML_Overview/Data_Types.md) | The horizontal scaling of the surface. |
| yscale | [Real](../../../GML_Overview/Data_Types.md) | The vertical scaling of the surface. |
| col | [Colour](../Colour_And_Alpha/Colour_And_Alpha.md) | The colour with which to blend the surface. |
| alpha | [Real](../../../GML_Overview/Data_Types.md) | The alpha of the surface. |

 

#### Returns:

N/A

 

#### Example:

draw\_surface\_tiled\_ext(surf, x, y, 2, 2, c\_red, 0\.5\);

This will draw the surface indexed in surf at the instance's own x and y position, double its stored size and tiled in every direction in the room, as well as blended with the colour red and partially transparent.
