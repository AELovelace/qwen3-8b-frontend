# room\_set\_viewport

This function sets the viewport properties for any room in your game *except the current one*.

You supply the room to set the viewport in, the viewport index (from 0 to 7\) and then whether the viewport should be visible at the start of the room or not (set to true to make the port visible, and false otherwise). After that you set the x and y coordinate (corresponding to the top left position of the viewport) and then the width and height in pixels.

 

#### Syntax:

room\_set\_viewport(rm, vind, vis, xport, yport, wport, hport)

| Argument | Type | Description |
| --- | --- | --- |
| rm | [Room Asset](../../../../The_Asset_Editors/Rooms.md) | The room to set |
| vind | [Real](../../../GML_Overview/Data_Types.md) | The index of the viewport to set |
| vis | [Boolean](../../../GML_Overview/Data_Types.md) | The visibility of the viewport (true is visible, false is invisible) |
| xport | [Real](../../../GML_Overview/Data_Types.md) | The x position of the viewport in the room |
| yport | [Real](../../../GML_Overview/Data_Types.md) | The y position of the viewport in the room |
| wport | [Real](../../../GML_Overview/Data_Types.md) | The width (in pixels) of the viewport |
| hport | [Real](../../../GML_Overview/Data_Types.md) | The height (in pixels) of the viewport |

 

#### Returns:

N/A

 

#### Example:

global.myroom \= room\_add();  

 room\_set\_width(global.myroom, 640\);  

 room\_set\_height(global.myroom, 480\);  

 room\_set\_viewport(global.myroom, 0, true, 0, 0, 640, 480\);

This will set the viewport \[0] properties in the room referenced in the variable global.myroom.
