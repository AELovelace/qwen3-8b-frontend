# ini\_key\_exists

This function checks to see if a key exists in the currently open ini and will return true if it does or false otherwise. This is not a necessary check to prevent errors as, when a key does not exist, reading from a non\-existent key will just return a default value. It can be useful to see if an ini file has saved specific data and a few other things, however.

 

#### Syntax:

ini\_key\_exists(section, key)

| Argument | Type | Description |
| --- | --- | --- |
| section |  | The section in the open .ini file to check a key in. |
| key |  | The key to check for. |

 

#### Returns:

 

#### Example:

ini\_open("savedata.ini");  

 if (!ini\_key\_exists("save1", "name"))   

 {  

     global.name \= "Player1";  

 }  

 ini\_close();

This will set variable global.name to "Player1" if no such key as "name" exists.
