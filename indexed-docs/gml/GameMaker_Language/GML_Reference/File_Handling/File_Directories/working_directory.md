# working\_directory

This variable holds the path to the directory where the game's files are stored.

In most cases, this is the same as the [program\_directory](program_directory.md), which is the path to the game's runner (executable). However, if the game's files happen to be in a different directory than the runner (say you use [game\_change](../../General_Game_Control/game_change.md) to use a different working directory or use command line to run a runner in a different location), then this will point to where the game files are, not the runner.

It may also be a different directory when testing your project through the IDE, as then the game files and the runner are in different locations as well.

When using this directory to write out a file, GameMaker will redirect it to the [game\_save\_id](../../General_Game_Control/game_save_id.md) location if the [file system sandbox](../../../../Additional_Information/The_File_System.md) does not allow writing to the working directory (this is the default behaviour, which can be disabled in the [Game Options](../../../../Settings/Game_Options.md) for Desktop targets only).

 
 
 
 

#### Syntax:

working\_directory

 

#### Returns:

[String](../../../GML_Overview/Data_Types.md)

 

#### Example:

ini\_open(working\_directory \+ "temp\_ini.ini");

This will open an INI file from the working directory of the game (creating it if it doesn't already exist). This could be the save area or the program directory depending on the sandbox level.
