# room\_duplicate

This function duplicates a given room and returns the duplicate's index to be used in all further calls to reference the new room.

 
 

#### Syntax:

room\_duplicate(index)

| Argument | Type | Description |
| --- | --- | --- |
| index | [Room Asset](../../../../The_Asset_Editors/Rooms.md) | The original room to be duplicated. |

 

#### Returns:

[Room Asset](../../../../The_Asset_Editors/Rooms.md)

 

#### Example:

global.myroom \= room\_duplicate(rm\_level);

This will duplicate the room rm\_level and assign the room index of this new room to the variable global.myroom.
