# room\_next

With this function you can retrieve the room *after* the room input into the function.

For example, you can use the variable [room](room.md) to get the current room and then use this function to find the room that follows it, as listed in [The Room Manager](../../../../Settings/The_Room_Manager.md).

If there is no room after the one you input then an invalid room handle (\-1) is returned.

 
 

#### Syntax:

room\_next(numb)

| Argument | Type | Description |
| --- | --- | --- |
| numb | [Room Asset](../../../../The_Asset_Editors/Rooms.md) | The room to get the next one after. |

 

#### Returns:

[Room Asset](../../../../The_Asset_Editors/Rooms.md)

 

#### Example:

if (room\_next(room) !\= \-1\)  

 {  

     room\_goto\_next();  

 }

The above code will check to see if the next room exists and if so, it will go to it.
