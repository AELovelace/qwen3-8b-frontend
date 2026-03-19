# texturegroup\_get\_sprites

This function retrieves the sprite index of each of the sprites assigned to texture pages within the given texture group.

You supply the texture group ID string (as defined in the [Texture Group Editor](../../../../Settings/Texture_Groups.md)) and the function will return a 1D array where each entry contains the sprite index for a sprite asset. If the function fails \- i.e.: an invalid group is given, or the group has no texture assigned to it \- then the array will be empty (0 length).

 

#### Syntax:

texturegroup\_get\_sprites(tex\_id)

| Argument | Type | Description |
| --- | --- | --- |
| tex\_id | [String](../../../GML_Overview/Data_Types.md) | The name of the texture group to check (a string) |

 

#### Returns:

[Array](../../../GML_Overview/Arrays.md) of [Sprite Asset](../../../../The_Asset_Editors/Sprites.md)

 

#### Example:

var \_tex\_array \= texturegroup\_get\_sprites( "MainMenu");  

 for (var i \= 0; i \< array\_length(\_tex\_array); \+\+i)  

 {  

     show\_debug\_message("Sprite " \+ string(i) \+ " Index:" \+ string(tex\_array\[i]));  

 }

The above code will retrieve the sprite indexes for the texture group "MainMenu", then display those IDs in the console output window.
