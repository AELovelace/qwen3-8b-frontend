# font\_get\_texture

This function returns a special *pointer* for the font texture page.

This value can then be used in other draw functions, particularly in general drawing when using [primitives](../../Drawing/Primitives/Primitives_And_Vertex_Formats.md) as well as the [Shader](../Shaders/Shaders.md) functions. You can get more information about the returned texture page using the different texture\_\* functions on the [Textures](../../Drawing/Textures/Textures.md) page.

 
 

#### Syntax:

font\_get\_texture(font)

 

| Argument | Type | Description |
| --- | --- | --- |
| font | [Font Asset](../../../../The_Asset_Editors/Fonts.md) | The font to use. |

 

#### Returns:

[Texture](../Sprites/Sprite_Information/sprite_get_texture.md)

 

#### Example:

tex \= font\_get\_texture(fnt\_Main);

The above code will get the texture pointer for the font indexed as fnt\_Main.
