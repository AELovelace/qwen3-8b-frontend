# title

With this action you can open an Ini file for reading and/or writing. If the Ini file does not exist at the location you are checking, GameMaker may create one, but *only* if you write data to it. If you have only read information from
 the Ini file, then the default values for the read function will be returned, but the Ini file will not actually be created.

Please note that you can only have *one Ini file open at any one time* and remember to use [Close Ini File](Close_Ini_File.md) once you're finished reading/writing from the Ini file as the information is not actually stored to disk
 until then (it is stored in memory until the file is closed).

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Filename | The name \- as a string and with the .ini extension \- of the file to open |

 

#### Example:

The above action block code will open an ini file for use, then get the value associated with
 the "name" key under the "player" header. If the name returned matches the default name value (ie: the file, section or key does *not* exist) then the file has a global variable written to it before being closed (and writing
 the new data to disk).
