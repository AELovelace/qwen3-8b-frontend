# sha1\_string\_utf8

This function will take an input UTF\-8 string (which has a variable number of bytes per character) and returns a 160 bit hash value in ASCII format. In this way you can generate a secure key which can be stored and used to check the integrity of the information being sent to (or received from) an external server (for example).

  There are two formats for the SHA\-1 encoding, UTF\-8 and Unicode. Both are provided to facilitate communication with different server setups, but the most common to use is Unicode.

 
 

#### Syntax:

sha1\_string\_utf8(string)

| Argument | Type | Description |
| --- | --- | --- |
| string | [String](../../../GML_Overview/Data_Types.md) | The string to generate the SHA\-1 hash for |

 

#### Returns:

[String](../../../GML_Overview/Data_Types.md)

 

#### Example:

var \_hash, \_str;  

 \_str \= json\_encode(hiscore\_map);  

 \_hash \= sha1\_string\_utf8(\_str);  

 ini\_open("local.ini");  

 ini\_write\_string("info", "0", \_hash);  

 ini\_close();  

 get\[0] \= http\_post\_string("http://www.macsweeneygames.com/CatchTheHaggis?game\_hiscores\=" \+ string(global.game\_id), \_str);

The above code will encode a DS map into a JSON string. A SHA\-1 hash is then generated and stored in an INI file so that this can later be used to check the integrity of the JSON should the same information be received later form the server. The JSON is then sent.
