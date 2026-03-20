# font\_get\_uvs

This function returns an [array](../../../GML_Overview/Arrays.md) with the UV coordinates for the font texture on the texture page, filling in the array with the following values:

- \[0] \= left
- \[1] \= top
- \[2] \= right
- \[3] \= bottom

This value can then be used in other draw functions, particularly in general drawing when using [primitives](../../Drawing/Primitives/Primitives_And_Vertex_Formats.md) as well as the [Shader](../Shaders/Shaders.md) functions.

 

#### Syntax:

font\_get\_uvs(font)

| Argument | Type | Description |
| --- | --- | --- |
| font | [Font Asset](../../../../The_Asset_Editors/Fonts.md) | The index of the font to use |

 

#### Returns:

[Array](../../../GML_Overview/Arrays.md)

 

#### Example:

var \_tex \= font\_get\_uvs(fnt\_main);  

 tex\_left \= \_tex\[0];  

 tex\_top \= \_tex\[1];  

 tex\_right \= \_tex\[2];  

 tex\_bottom \= \_tex\[3];

The above code will store the UV coordinates for the given font in a local array and then assign the values to instance variables.
