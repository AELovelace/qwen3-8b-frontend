# game\_display\_name

This **read only** variable returns the display name of your game for the target platform, as set in the [Game Options](../../../Settings/Game_Options.md).

 

#### Syntax:

game\_display\_name

 

#### Returns:

 

#### Example:

var name \= game\_display\_name;  
 var ver \= string(GM\_version);  
 draw\_text(32, 32, name \+ ":" \+ ver);

The above code gets the display name and the version number of the game and draws them.
