# font\_set\_cache\_size

This function sets how many blended copies of the given font can be cached before old ones are overwritten.

When performing image blending and colouring, HTML5 cannot do it dynamically in the same way an executable could be performed. Therefore GameMaker has to temporarily save a blended copy of the images and load them in when needed.

The default value is 4\.

**NOTE** for sprite fonts you should be using the equivalent function for sprites, [sprite\_set\_cache\_size()](../Sprites/Sprite_Manipulation/sprite_set_cache_size.md).

 

#### Syntax:

font\_set\_cache\_size(ind, max)

 

| Argument | Type | Description |
| --- | --- | --- |
| ind | [Font Asset](../../../../The_Asset_Editors/Fonts.md) | The index of the font to change the cache size of. |
| max | [Real](../../../GML_Overview/Data_Types.md) | The maximum number of cached copies of the font that can be stored. |

 

#### Returns:

N/A

 

#### Example:

font\_set\_cache\_size(fnt\_MainMenu, 2\);

This will set the font cache of the font indexed in the variable "fnt\_MainMenu" to 2 copies.
