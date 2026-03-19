# room\_set\_height

This function changes (or sets) the height of any room in your game *except the current one*.

 

#### Syntax:

room\_set\_height(index, h)

| Argument | Type | Description |
| --- | --- | --- |
| index | [Room Asset](../../../../The_Asset_Editors/Rooms.md) | The room to set the height of. |
| h | [Real](../../../GML_Overview/Data_Types.md) | The new height of the room in pixels. |

 

#### Returns:

N/A

 

#### Example:

global.myroom \= room\_add();  

 room\_set\_width(global.myroom, 640\);  

 room\_set\_height(global.myroom, 480\);  

 room\_set\_persistent(global.myroom, false);

This will create a new room and store its index in the variable global.myroom. It will then set its width to 640 pixels, its height to 480 pixels, its caption to and its persistence to false.
