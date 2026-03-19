# room\_goto\_next

With this function you can make your game go to the next room as listed in the [Room Manager](../../../../Settings/The_Room_Manager.md) at the time the game was compiled. If this room does not exist, an error will be thrown and the game will be forced to close. Note that the room will not change until the end of the event where the function was called, so any code after this has been called will still run if in the same event.

 
 

#### Syntax:

room\_goto\_next()

 

#### Returns:

N/A

 

#### Example:

if (room\_exists(room\_next(room)))  

 {  

     room\_goto\_next();  

 }

The above code will check to see if there is another room after the current one and if so it will go to that room.
