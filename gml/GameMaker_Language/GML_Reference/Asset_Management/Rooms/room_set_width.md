# room\_set\_width

This function changes (or sets) the width of any room in your game *except the current one*.

 

#### Syntax:

room\_set\_width(index, w)

| Argument | Type | Description |
| --- | --- | --- |
| index | [Room Asset](../../../../The_Asset_Editors/Rooms.md) | The room to set the width of. |
| w | [Real](../../../GML_Overview/Data_Types.md) | The new width of the room in pixels. |

 

#### Returns:

N/A

 

#### Example:

global.myroom \= room\_add();  

 room\_set\_width(global.myroom, 640\);  

 room\_set\_height(global.myroom, 480\);  

 room\_set\_persistent(global.myroom, false);

This will create a new room and store its index in the variable global.myroom. It will then set its width to 640 pixels, its height to 480 pixels and its persistence to false.
