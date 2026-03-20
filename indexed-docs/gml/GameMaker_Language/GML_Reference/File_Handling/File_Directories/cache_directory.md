# cache\_directory

This variable holds the path to the cache directory for your game. Use this directory to store cached data that is not permanently needed for your game.

On some consoles, certain options may need to be enabled for this to hold a valid path.

 
 

#### Syntax:

cache\_directory

 

#### Returns:

[String](../../../GML_Overview/Data_Types.md)

 

#### Example:

ini\_open(cache\_directory \+ "cache\_ini.ini");

This will open an INI file in the cache directory of the game (creating it if it doesn't already exist).
