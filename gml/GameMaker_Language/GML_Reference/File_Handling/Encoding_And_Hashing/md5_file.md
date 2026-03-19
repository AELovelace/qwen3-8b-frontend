# md5\_file

This function generates a unique MD5 hash for the given file which can be stored for later use.

 
 

#### Syntax:

md5\_file(filename)

| Argument | Type | Description |
| --- | --- | --- |
| filename | [String](../../../GML_Overview/Data_Types.md) | The file to generate the MD5 hash for |

 

#### Returns:

[String](../../../GML_Overview/Data_Types.md)

 

#### Example:

hash \= md5\_file(working\_directory \+ "game\_data.ini");

The above code will generate an MD5 hash for the specified file and store the returned value in the variable hash.
