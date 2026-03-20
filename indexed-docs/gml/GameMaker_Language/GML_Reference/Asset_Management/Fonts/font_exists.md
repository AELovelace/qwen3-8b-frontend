# font\_exists

This function returns whether a font with the specified index exists or not. You can check font indices as defined from the Asset Browser, or fonts that have been added using functions like font\_add().

 

#### Syntax:

font\_exists(ind)

| Argument | Type | Description |
| --- | --- | --- |
| ind | [Font Asset](../../../../../The_Asset_Editors/Fonts.md) | Index of the font to check. |

 

#### Returns:

[Boolean](../../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

if (font\_exists(fnt\_Main))   

 {  

     draw\_set\_font(fnt\_Main);  

 }

This will set the active drawing font to fnt\_Main if it exists.
