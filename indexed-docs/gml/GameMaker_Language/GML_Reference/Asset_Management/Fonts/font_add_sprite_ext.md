# font\_add\_sprite\_ext

With this function you can use a [sprite strip](../../../../The_Asset_Editors/Sprite_Properties/Sprite_Strips.md) (the sprite itself **must** be a sprite asset from [The Asset Browser](../../../../Introduction/The_Asset_Browser.md), or a sprite you have added to the game assets using [sprite\_add](../Sprites/Sprite_Manipulation/sprite_add.md)) to create a new font asset, where each sub\-image would be an individual symbol or letter. Unlike the normal [font\_add\_sprite](font_add_sprite.md) which has a specific order for the sub\-images of the sprite, this function will map the sprite sub\-images based on the function's string\_map argument. This argument is a string that you can use to tell GameMaker what order the sub\-images of the sprite font are and it will map these automatically when writing text. So, for example, if you have a string\-map of "AaBbCcDdEeFfGgHh", your sprite font *must* have the sub\-images ordered in this way. You can define "space" as being any character you want, for example a single line the size that you want the space to be, and all spaces in text will be rendered at that width (but the image chosen will *never* be rendered), or if you don't supply a sprite for space then the width of the widest character in the sprite font will be used instead.

You can also set the spacing for the font to be proportional (true) or not (false), where a proportional font is spaced based on the actual width of the letters (so the letter "i" takes less room than the letter "w", for example) while a non\-proportional font will be spaced based on the sub\-image width, like a monospaced font. Finally, you can define the space to leave between each letter when writing, and this can be any integer value, with 0 being no space (the letters will "touch" if proportional).

 
The function returns a handle that should be stored in a variable as this will be needed in all further codes that refer to this font.  

It is worth noting that for the font alignment functions to work (like [draw\_set\_halign](../../Drawing/Text/draw_set_halign.md)) then the font sprite should have its origin set to the *top left corner*. If you use other values then you will need to take the origin offset into consideration when drawing text using the font.

 
 

#### Syntax:

font\_add\_sprite\_ext(spr, string\_map, prop, sep)

| Argument | Type | Description |
| --- | --- | --- |
| spr | [Sprite Asset](../../../../The_Asset_Editors/Sprites.md) | The sprite to add a font based on. |
| string\_map | [String](../../../GML_Overview/Data_Types.md) | String from which sprite sub\-image order is taken. |
| prop | [Boolean](../../../GML_Overview/Data_Types.md) | Set as proportional font or not. |
| sep | [Real](../../../GML_Overview/Data_Types.md) | The space to leave between each letter. |

 

#### Returns:

[Font Asset](../../../../The_Asset_Editors/Fonts.md)

 

#### Example:

global.font \= font\_add\_sprite\_ext(spr\_CalcFont, "0123456789\+\-\*/\=", true, 2\);

The above code will create a new font asset from the sprite indexed in the variable spr\_CalcFont and store the handle of the new font in the variable global.font. The sub\-images of the sprite font will be mapped to the string specified.
