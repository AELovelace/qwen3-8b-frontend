# texture\_get\_width

This function returns the width of the texture with the given ID, which is always a value within the range 0 \- 1\. This can then be used when mapping textures to models or primitives.

 

#### Syntax:

texture\_get\_width(tex)

| Argument | Type | Description |
| --- | --- | --- |
| tex | [Texture](../../Asset_Management/Sprites/Sprite_Information/sprite_get_texture.md) | The texture page asset pointer to use |

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

tex\_w \= texture\_get\_width(sprite\_get\_texture(spr\_Model\_tex, 0\));

The above code will get the width of the texture taken from a sprite asset.
