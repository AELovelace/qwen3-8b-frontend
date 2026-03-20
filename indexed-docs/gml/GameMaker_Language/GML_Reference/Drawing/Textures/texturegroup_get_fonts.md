# texturegroup\_get\_fonts

This function retrieves the font index of each of the fonts assigned to texture pages within the given texture group.

You supply the texture group ID string (as defined in the [Texture Group Editor](../../../../Settings/Texture_Groups.md)) and the function will return a 1D array where each entry contains the font index for a font asset. If the function fails \- i.e.: an invalid group is given, or the group has no texture assigned to it \- then the array will be empty (0 length).

 

#### Syntax:

texturegroup\_get\_fonts(tex\_id)

| Argument | Type | Description |
| --- | --- | --- |
| tex\_id | [String](../../../GML_Overview/Data_Types.md) | The name of the texture group to check (a string) |

 

#### Returns:

[Array](../../../GML_Overview/Arrays.md) of [Font Asset](../../../../The_Asset_Editors/Fonts.md)

 

#### Example:

var \_tex\_array \= texturegroup\_get\_fonts( "MainMenu");  

 for (var i \= 0; i \< array\_length(\_tex\_array); \+\+i)  

 {  

     show\_debug\_message("Font " \+ string(i) \+ " Index:" \+ string(tex\_array\[i]));  

 }

The above code will retrieve the font indexes for the texture group "MainMenu", then display those IDs in the console output window.
