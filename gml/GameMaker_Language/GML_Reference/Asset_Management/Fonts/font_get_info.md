# font\_get\_info

This function is used to retrieve information for the given font. You supply a font index, which can be an asset added through [The Asset Browser](../../../../Introduction/The_Asset_Browser.md) or a font [added](font_add.md) at runtime.

The function returns a [struct](../../../GML_Overview/Structs.md) with the following variables:

| [Font Info Struct](font_get_info.md) | | |
| --- | --- | --- |
| Variable Name | Data Type | Description |
| ascender | [Real](../../../GML_Overview/Data_Types.md) | The height of the font's [ascender](https://en.wikipedia.org/wiki/Ascender_(typography)) (in pixels) |
| ascenderOffset | [Real](../../../GML_Overview/Data_Types.md) | The maximum offset from the baseline to the top of the font (in pixels) |
| size | [Real](../../../GML_Overview/Data_Types.md) | The approximate size of the font (in pixels) |
| spriteIndex | [Sprite Asset](../../../../The_Asset_Editors/Sprites.md) | The sprite index for the font if it was [created from a sprite](font_add_sprite.md), otherwise an invalid sprite handle (\-1\) |
| texture | [Real](../../../GML_Overview/Data_Types.md) | \-1 if the font was created from a sprite, otherwise the texture ID of the font |
| name | [String](../../../GML_Overview/Data_Types.md) | The name of the font |
| bold | [Boolean](../../../GML_Overview/Data_Types.md) | true if the font is bold, otherwise false *(see **NOTE** below)* |
| italic | [Boolean](../../../GML_Overview/Data_Types.md) | true if the font is italic, otherwise false *(see **NOTE** below)* |
| glyphs | [Font Glyph Struct](font_get_info.md) | A struct containing information for each glyph in the font (more information is given [below](#glyphs)) |
| sdfEnabled | [Boolean](../../../GML_Overview/Data_Types.md) | Whether SDF is enabled or disabled for this font |
| sdfSpread | [Real](../../../GML_Overview/Data_Types.md) | The SDF spread value set for this font |
| effectsEnabled | [Boolean](../../../GML_Overview/Data_Types.md) | Whether effects are enabled for this font |
| effectParams | [Struct](../../../GML_Overview/Structs.md) | The effects struct for this font, which can be changed with [font\_enable\_effects](font_enable_effects.md) |

  The **bold** and italic variables only reflect the user's settings for the font, so they may not be accurate for fonts that appear bold or italic by default.

If the supplied font doesn't exist, the function will return undefined.

Also note that changing the values of any of these variables, or any variables contained within the glyphs struct, will not change how the font is rendered, so this information should be considered **read\-only**.

## Glyphs Struct

The glyphs variable in the returned struct will be a struct on its own, containing information for each glyph included in the font. Each variable in this struct will be a glyph's character name, which will hold a struct containing information for that glyph. You can imagine these nested structs in the following format (starting from the main struct):

{  

     glyphs:  

     {  

         A: {},  

         B: {},  

         C: {},  

         // ...other glyphs  

     },  

     // ...other font info  

 }

You can use a glyph's character name to retrieve its information from the struct, such as in the following code:

var \_font\_info \= font\_get\_info(Font1\);  

  

 var \_info\_A \= \_font\_info.glyphs\[$ "A"]; // $ is a struct accessor  

  

 show\_debug\_message(\_info\_A);
 

The code above gets the glyph struct for the "A" character and prints it to the output log. You can also replace the string ("A") with a variable that holds a string, which will allow you to get information for any glyph through that variable at runtime.

The struct returned for a glyph will contain the following variables:

  On HTML5, the glyphs struct will be empty for any loaded file fonts (such as \*.ttf or \*.otf) as the runtime will not have information on those glyphs.

| [Font Glyph Struct](font_get_info.md) | | |
| --- | --- | --- |
| Variable Name | Data Type | Description |
| char | [Real](../../../GML_Overview/Data_Types.md) | If the font was created from a sprite, this will be the image index of the glyph from that sprite, otherwise it will be its Unicode character number  ***Note**: All variables below this will not be present in the struct if the font was created from a sprite* |
| x | [Real](../../../GML_Overview/Data_Types.md) | The X position of the glyph on the texture page (in pixels) |
| y | [Real](../../../GML_Overview/Data_Types.md) | The Y position of the glyph on the texture page (in pixels) |
| w | [Real](../../../GML_Overview/Data_Types.md) | The width of the glyph on the texture page (in pixels) |
| h | [Real](../../../GML_Overview/Data_Types.md) | The height of the glyph on the texture page (in pixels) |
| shift | [Real](../../../GML_Overview/Data_Types.md) | The number of pixels to shift right when advancing to the next character (can be negative for shifting left) |
| offset | [Real](../../../GML_Overview/Data_Types.md) | The number of pixels to horizontally offset the rendering of this glyph without affecting the shift position (can be positive or negative) |
| yoffset | [Real](../../../GML_Overview/Data_Types.md) | The number of pixels to vertically offset the rendering of this glyph without affecting the shift position (can be positive or negative) |
| kerning | [Array](../../../GML_Overview/Arrays.md) | An array of integers containing kerning information in pairs (or groups of 2\). The first integer in a pair is the Unicode value for a character, and the second integer is the amount to add to that character's shift value (can be positive or negative) if it is preceded by this glyph's character. |

  For file fonts loaded at runtime, the x and y values for a glyph may be \-1 if it hasn't been rendered yet, as it will have no position on the texture page used for caching.

 

#### Syntax:

font\_get\_info(font)

| Argument | Type | Description |
| --- | --- | --- |
| font | [Font Asset](../../../../The_Asset_Editors/Fonts.md) | The font for which information should be retrieved. |

 

#### Returns:

[Font Info Struct](font_get_info.md) (or undefined)

 

#### Example:

var \_info \= font\_get\_info(my\_font);  

  

 if (\_info !\= undefined \&\& \_info.bold)  

 {  

     image\_xscale \*\= 2;  

     image\_yscale \*\= 2;  

 }
 

This code retrieves information for the font stored in the my\_font variable. If the returned value is **not** undefined and the given font is bold, the instance's scale is doubled.
