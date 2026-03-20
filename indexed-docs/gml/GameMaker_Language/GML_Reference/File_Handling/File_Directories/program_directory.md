# program\_directory

This variable holds the path to the directory where the game's runner (executable) is stored. However, this may not always be useful, particularly as some devices run the executable from a \*.zip file, so this would return that location no matter where the extracted executable is actually running from.

This is different from [working\_directory](working_directory.md), which stores where the game's files are stored, however by default they are in the same location.

 
 
 
 

#### Syntax:

program\_directory

 

#### Returns:

[String](../../../GML_Overview/Data_Types.md)

 

#### Example:

dir \= program\_directory;

This will store the directory where the executable is stored in a variable.
