# sprite\_replace

This function works in almost the exact same manner as [sprite\_add](sprite_add.md), only instead of returning the handle of the sprite you are importing, it overwrites a previously created sprite index.

When using this function you should use a sprite index that has been created and stored in a variable using other functions like [sprite\_add](sprite_add.md) or [sprite\_create\_from\_surface](sprite_create_from_surface.md), or even [sprite\_duplicate](sprite_duplicate.md), rather than a resource tree sprite asset.

You *can* replace a sprite from the game assets using this function, but doing so means that you will lose the reference ID for the sprite that you are replacing, regardless of whether you call [game\_restart](../../../General_Game_Control/game_restart.md) or not, and so this is not recommended.

Regardless of the sprite being replaced, this function will **create a new texture page for the sprite** and so care should be taken when using it as it may adversely affect performance by increasing the number of required texture swaps for rendering.

For information on the arguments, see [sprite\_add](sprite_add.md).

### Platform\-specific notes

- You should be aware that if you are using this function in your **HTML5** target game to load resources from an external server, then, due to XSS protection in browsers, attempts to load resources from across domains can be blocked and may appear to return blank results.

 
 

#### Syntax:

sprite\_replace(ind, fname, imgnumb, removeback, smooth, xorig, yorig)

| Argument | Type | Description |
| --- | --- | --- |
| ind | [Sprite Asset](../../../../../The_Asset_Editors/Sprites.md) | The sprite to permanently replace |
| fname | [String](../../../../GML_Overview/Data_Types.md) | The name (a file path) of the file to add or a data URL with the image data embedded in the string (encoded in [base64](https://en.wikipedia.org/wiki/Base64)) |
| imgnumb | [Real](../../../../GML_Overview/Data_Types.md) | The number of frames the sprite will be cut up into horizontally. Use 1 for one single image or \*.gif |
| removeback | [Boolean](../../../../GML_Overview/Data_Types.md) | Indicates whether to make all pixels with the background colour (left\-bottom pixel) transparent |
| smooth | [Boolean](../../../../GML_Overview/Data_Types.md) | Indicates whether to smooth the edges |
| xorig | [Real](../../../../GML_Overview/Data_Types.md) | The x coordinate of the origin, relative to the sprite's top left corner |
| yorig | [Real](../../../../GML_Overview/Data_Types.md) | The y coordinate of the origin, relative to the sprite's top left corner |

 

#### Returns

N/A

 

#### Example:

sprite\_replace(spr\_banner, "gravemaker.png", 1, false, false, 0, 0\);

The above code will replace the image asset referenced in spr\_banner with another one loaded from an external source.
