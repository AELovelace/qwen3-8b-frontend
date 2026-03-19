# sha1\_string\_unicode

This function will take an input Unicode string and returns a 160 bit hash value in ASCII format. In this way you can generate a secure key which can be stored and used to check the integrity of the information being sent to (or received from) an external server (for example).

  There are two formats for the SHA\-1 encoding, UTF\-8 and Unicode. Both are provided to facilitate communication with different server setups, but the most common to use is Unicode.

 
 

#### Syntax:

sha1\_string\_unicode(string)

| Argument | Type | Description |
| --- | --- | --- |
| string | [String](../../../GML_Overview/Data_Types.md) | The string to generate the SHA\-1 hash for |

 

#### Returns:

[String](../../../GML_Overview/Data_Types.md)

 

#### Example:

var \_hash, \_str;  

 \_str \= base64\_encode(game\_data);  

 \_hash \= sha1\_string\_unicode(\_str);  

 http\_get("http://www.macsweeneygames.com/CatchTheHaggis/gamedata?hash\=" \+ \_hash);  

 http\_get("http://www.macsweeneygames.com/CatchTheHaggis/gamedata?data\=" \+ \_str);

The above code will base64 encode a string and then generate an SHA\-1 hash. Finally, both the hash and the encoded string are sent to a server.
