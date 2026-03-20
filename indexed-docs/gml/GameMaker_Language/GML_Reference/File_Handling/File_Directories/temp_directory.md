# temp\_directory

This variable holds the path to the temporary directory created for your game each time it is run.

This directory will hold files and can be accessed while the game is running, but it will be removed (along with all files that it contains) when the game is closed.

 
 

#### Syntax:

temp\_directory

 

#### Returns:

[String](../../../GML_Overview/Data_Types.md)

 

#### Example:

ini\_open(temp\_directory \+ "temp\_ini.ini");

This will open an INI file in the temporary directory of the game (creating it if it doesn't already exist).
