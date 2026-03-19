# font\_sdf\_spread

This function is used to change the spread value of an [SDF\-enabled font](font_enable_sdf.md). The spread limits how much [font effects](font_enable_effects.md) can spread from a glyph's edge.

The spread value is the distance (in pixels) that the signed distance field extends from the edge of each glyph. The spread can be between 2 and 32 pixels (inclusive), and the default is 8\.

This is also useful for running custom shaders on your text, as a larger spread value will allow for effects with larger radii (such as glows). However a larger spread value will mean that the font will take up more space on the texture page. In contrast, a smaller spread value will save texture space, and also improve rendering precision.

 

#### Syntax:

font\_sdf\_spread(ind, spread)

| Argument | Type | Description |
| --- | --- | --- |
| ind | [Font Asset](../../../../../The_Asset_Editors/Fonts.md) | The index of the font (must be [SDF\-enabled](font_enable_sdf.md)) |
| spread | [Real](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The new spread value, between 2 and 32 pixels (inclusive) |

 

#### Returns:

N/A

 

#### Example:

new\_font \= font\_add("STENCIL.TTF", 32, false, false, 32, 128\);  

 font\_enable\_sdf(new\_font, true);  

font\_sdf\_spread(new\_font, 16\);
 

This will load a font from an included TTF file, enable SDF for it and set its spread value to 16 pixels.
