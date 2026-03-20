# sprite\_set\_cache\_size\_ext

This function is used on HTML5 to set how many blended copies of the given sprite can be cached before old ones are overwritten (default is 4\). This is applied to the given sub\-image of the sprite.

When performing image blending, HTML5 cannot do it dynamically in the same way an executable could be performed. Therefore, GameMaker has to temporarily save a blended copy of the image and load it in.

 

#### Syntax:

sprite\_set\_cache\_size\_ext(ind, index, max)

| Argument | Type | Description |
| --- | --- | --- |
| ind | [Sprite Asset](../../../../../The_Asset_Editors/Sprites.md) | The index of the sprite to change the cache size of |
| index | [Real](../../../../GML_Overview/Data_Types.md) | The sub\-image of ind to change the cache size of |
| max | [Real](../../../../GML_Overview/Data_Types.md) | The maximum number of cached copies of the sprite that can be stored |

 

#### Returns

N/A

 

#### Example:

sprite\_set\_cache\_size\_ext(sprite0, 0, 2\);

This will set the sprite cache of the first sub\-image of sprite0 to 2 copies.
