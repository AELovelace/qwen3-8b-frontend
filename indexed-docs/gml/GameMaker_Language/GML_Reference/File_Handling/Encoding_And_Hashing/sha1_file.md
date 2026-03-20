# sha1\_file

This function will take an input file and return a 160 bit hash value in ASCII format unique to that file to be used for integrity verification at any later date.

 
 

#### Syntax:

sha1\_file(filename)

| Argument | Type | Description |
| --- | --- | --- |
| filename | [String](../../../GML_Overview/Data_Types.md) | The file to generate the SHA\-1 hash for |

 

#### Returns:

[String](../../../GML_Overview/Data_Types.md)

 

#### Example:

hash \= sha1\_file(working\_directory \+ "game\_data.ini");

The above code will generate a sha1 hash for the specified file and store the returned value in the variable hash.
