# room\_add

This function creates a new, empty, room and adds it to your game, returning its index to be stored in a variable for all further code that deal with this room.

Each room added in this way is permanently added to the game until the executable is closed, i.e.: *rooms added through code cannot be deleted again*. This has important implications for memory use and so you should use this function with care.

 
 

#### Syntax:

room\_add()

 

#### Returns:

[Room Asset](../../../../The_Asset_Editors/Rooms.md)

 

#### Example:

global.myroom \= room\_add();  

 room\_set\_width(global.myroom, 1280\);  

 room\_set\_height(global.myroom, 720\);  

 room\_set\_persistent(global.myroom, false);

This will create a new room and store it in the variable global.myroom. It will then set its width to 1280 pixels, its height to 720 pixels, and its persistence to false.
