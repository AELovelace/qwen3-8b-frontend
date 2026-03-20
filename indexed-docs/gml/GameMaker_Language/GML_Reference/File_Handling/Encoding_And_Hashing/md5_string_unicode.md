# md5\_string\_unicode

This function will take an input Unicode string (which is 16bits for each character) and return the 32\-character hexadecimal MD5 hash that is unique to that string. In this way you can generate a secure key which can be stored and used to check the integrity of the information being sent to (or received from) an external server (for example).

  There are two formats for the MD5 encoding, UTF\-8 and Unicode. Both are provided to facilitate communication with different server setups, but the most common to use is Unicode.

 
 

#### Syntax:

md5\_string\_unicode(string)

| Argument | Type | Description |
| --- | --- | --- |
| string | [String](../../../GML_Overview/Data_Types.md) | The string to hash |

 

#### Returns:

[String](../../../GML_Overview/Data_Types.md)

 

#### Example:

var \_hash, \_str;  

 \_str \= base64\_encode(game\_data);  

 \_hash \= md5\_string\_unicode(\_str);  

 http\_get("http://www.macsweeneygames.com/catchthehaggis/gamedata?hash\=" \+ \_hash);  

 http\_get("http://www.macsweeneygames.com/CatchTheHaggis/gamedata?data\=" \+ \_str);

The above code will base64 encode a string and then generate an MD5 hash. Finally, both the hash and the encoded string are sent to a server.
