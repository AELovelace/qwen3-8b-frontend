# vertex\_colour

If your defined vertex format takes a colour value you can use this function to add that data to the vertex being defined for the current primitive.

The function needs a buffer to store the data in and will take either a [colour constant](../Colour_And_Alpha/Colour_And_Alpha.md), or a hex value (using the standard GameMaker format of BGR, e.g.: $FF0000 for blue) as well as an alpha value from 0 (transparent) to 1 (fully opaque).

 

#### Syntax:

vertex\_colour(buffer, colour, alpha)

| Argument | Type | Description |
| --- | --- | --- |
| buffer | [Vertex Buffer](../../../../../GameMaker_Language/GML_Reference/Drawing/Primitives/vertex_create_buffer.md) | The vertex buffer to write the information to. |
| colour | [Colour](../../../../../GameMaker_Language/GML_Reference/Drawing/Colour_And_Alpha/Colour_And_Alpha.md) | The colour for this vertex (can be a constant or a hex value). |
| alpha | [Real](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The alpha value for the vertex (from 0 to 1\). |

 

#### Returns:

N/A

 

#### Example:

vertex\_colour(b, c\_white, 1\);

The above code will set the colour of the current vertex being defined to white with an alpha value of 1\.
