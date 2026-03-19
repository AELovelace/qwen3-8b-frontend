# ini\_open

This function opens a new INI file for reading/writing, closing the currently open INI file if there is any.

If no INI file with the given name exists at the location you are checking, GameMaker may create it, but only if you write data to it. If you have only read information from the INI file, then the default values for the read function will be returned, but the INI file will *not* actually be created.

You can only have **one** INI file open at any one time and remember to use [ini\_close](ini_close.md) once you're finished reading from/writing to the INI file as the information is not actually saved to disk until then (it is also stored in memory until the file is closed). Note, however, that calling ini\_open with an INI file still open will close that file.

 
 

#### Syntax:

ini\_open(name)

| Argument | Type | Description |
| --- | --- | --- |
| name | [String](../../../GML_Overview/Data_Types.md) | The filename for the INI file |

 

#### Returns:

N/A

 

#### Example:

ini\_open("Settings/savedata.ini");  

 score \= ini\_read\_real("save1", "score", 0\);  

 ini\_close();

This will open "savedata.ini" and read the score value under the section "save1" with the key "score" in it, then close the INI again. Should there be no value under "save1", "score" or there is no "savedata.ini" file present, score will be set to 0 (the default value). Note that the INI file has been placed in the sub\-directory "Settings", which is the folder that holds the INI file in the Asset Browser included files.
