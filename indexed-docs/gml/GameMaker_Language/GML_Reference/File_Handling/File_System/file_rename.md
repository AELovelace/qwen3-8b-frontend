# file\_rename

This function will rename the specified file with the specified name. The function will return true if the file has successfully been renamed, or false in any other circumstances.

 
 

#### Syntax:

file\_rename(oldname, newname)

| Argument | Type | Description |
| --- | --- | --- |
| oldname | [String](../../../GML_Overview/Data_Types.md) | The name of the file to change |
| newname | [String](../../../GML_Overview/Data_Types.md) | The new name to give the file |

 

#### Returns:

[Boolean](../../../GML_Overview/Data_Types.md)

 

#### Example:

if (file\_exists("level1\.txt"))  

 {  

     file\_rename("level1\.txt", "level.txt");  

 }

This would check for a file and if it exists it is renamed.
