# font\_cache\_glyph

This function lets you pre\-cache a character glyph from a font.

If you don't pre\-cache a character using this function, it's automatically cached before it's drawn for the first time.

This function returns a struct with the x and y position of the glyph on the font's texture page, e.g. { x : 208, y : 62 }. To get a handle to the texture page that the cached glyph is on you can use [font\_get\_texture](font_get_texture.md).

 

#### Syntax:

font\_cache\_glyph(font, glyph\_index)

| Argument | Type | Description |
| --- | --- | --- |
| font | [Font Asset](../../../../../The_Asset_Editors/Fonts.md) | The font to cache a character or glyph from |
| glyph\_index | [Real](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The index (or character code) of the glyph to cache (see [ord](../../Strings/ord.md)/[string\_ord\_at](../../Strings/string_ord_at.md)) |

 

#### Returns:

[Struct](../../../../../GameMaker_Language/GML_Overview/Structs.md)

 

#### Example:

var \_glyph \= font\_cache\_glyph(fnt\_gui, 65\);

The above code caches the glyph with the index 65 from a font asset, and stores the returned struct in a local variable.
