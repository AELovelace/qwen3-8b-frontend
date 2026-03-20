# surface\_getpixel

This function can be used to get the colour of a specific pixel from a surface, using the local coordinates of the surface where (0, 0\) is the top left corner. This function should *not* be used very often as it is extremely slow and may cause a pause in your game.

The data type returned by this function will depend on the [format](surface_create.md) of the given surface:

| Formats | Function Return |
| --- | --- |
| surface\_rgba8unorm (default) surface\_rgba4unorm  surface\_r8unorm  surface\_rg8unorm | For these formats, the function will return a regular [colour](../Colour_And_Alpha/Colour_And_Alpha.md) value. Any unused channels are set to 0\. |
| surface\_rgba16float  surface\_r16float  surface\_rgba32float  surface\_r32float | For these formats, the function will return an array with 3 values (R, G, B) with each being a 32\-bit float. Any unused channels are set to 0\.   To get the pixel colour with the alpha channel, use [surface\_getpixel\_ext](surface_getpixel_ext.md). |

 
 

#### Syntax:

surface\_getpixel(surface\_id, x, y)

| Argument | Type | Description |
| --- | --- | --- |
| surface\_id | [Surface](../../../../../GameMaker_Language/GML_Reference/Drawing/Surfaces/surface_create.md) | The surface. |
| x | [Real](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The x position on the surface to get the pixel from. |
| y | [Real](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The y position on the surface to get the pixel from. |

 

#### Returns:

[Colour](../../../../../GameMaker_Language/GML_Reference/Drawing/Colour_And_Alpha/Colour_And_Alpha.md) or [Array](../../../../../GameMaker_Language/GML_Overview/Arrays.md)

 

#### Example:

col \= surface\_getpixel(surf, 56, 78\);

This will return the colour of the pixel at coordinates (56, 78\) of the surface stored in the variable surf.
