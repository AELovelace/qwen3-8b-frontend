# ini\_open\_from\_string

This function creates a temporary INI file from a string and opens it for reading/writing. The string should be correctly formatted as an INI file (i.e.: with sections, line breaks, keys and values), otherwise the INI file will not be created correctly.

Note that this INI file is temporary and will be removed from memory the moment it is closed, losing any information that was stored in it, however the [ini\_close](ini_close.md) function returns a string of the full INI file which can then be saved to a server or to disk.

 

#### Syntax:

ini\_open\_from\_string(string)

| Argument | Type | Description |
| --- | --- | --- |
| string | [String](../../../GML_Overview/Data_Types.md) | The string containing all the INI information |

 

#### Returns:

N/A

 

#### Example:

ini\_open\_from\_string(str);  

 global.sound \= ini\_read\_string("Options", "Sound", true);  

 ini\_close();

The above code sets a temporary INI to hold the information from the string str, then reads from the INI before closing it again.
