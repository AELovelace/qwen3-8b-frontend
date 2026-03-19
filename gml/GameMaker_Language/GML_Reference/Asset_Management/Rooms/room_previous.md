# room\_previous

With this function you can retrieve the room *before* the room input into the function.

For example, you can use the variable [room](room.md) to get the current room and then use this function to find the room that comes before it, as listed in [The Room Manager](../../../../Settings/The_Room_Manager.md).

If there is no room before the one you input then an invalid room handle (\-1) is returned.

 
 

#### Syntax:

room\_previous(numb)

| Argument | Type | Description |
| --- | --- | --- |
| numb | [Room Asset](../../../../The_Asset_Editors/Rooms.md) | The room to get the one before from. |

 

#### Returns:

[Room Asset](../../../../The_Asset_Editors/Rooms.md)

 

#### Example:

if (room\_previous(room) !\= \-1\)  

 {  

     room\_goto\_previous();  

 }

The above code will check to see if the previous room exists and if so, it will go to it.
