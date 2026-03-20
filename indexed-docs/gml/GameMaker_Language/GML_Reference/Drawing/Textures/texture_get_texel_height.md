# texture\_get\_texel\_height

This function returns the height of a single texel from the texture page of the image asset used.

A texel, or *texture element*, is the fundamental unit of texture space used in computer graphics. Textures are represented by arrays of texels, just as pictures are represented by arrays of pixels.

 

#### Syntax:

texture\_get\_texel\_height(tex)

| Argument | Type | Description |
| --- | --- | --- |
| tex | [Texture](../../Asset_Management/Sprites/Sprite_Information/sprite_get_texture.md) | The texture page asset pointer to use |

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

var \_tex \= sprite\_get\_texture(sprite\_index, 0\);  

 tex\_w \= texture\_get\_texel\_width(\_tex);  

 tex\_h \= texture\_get\_texel\_height(\_tex);

The above code will get the texel width and height of the texture taken from a sprite asset.
