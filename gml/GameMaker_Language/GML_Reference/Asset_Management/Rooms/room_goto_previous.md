# room\_goto\_previous

With this function you can make your game go to the previous room as listed in the [Room Manager](../../../../Settings/The_Room_Manager.md) at the time the game was compiled. If this room does not exist, an error will be thrown and the game will be forced to close. Note that the room will not change until the end of the event where the function was called, so any code after this has been called will still run if in the same event. This function will also trigger the **Room End** event.

 
 

#### Syntax:

room\_goto\_previous()

 

#### Returns:

N/A

 

#### Example:

if (room\_exists(room\_previous(room)))  

 {  

     room\_goto\_previous();  

 }

The above code will check to see if there is another room before the current one and if so it will go to that room.
