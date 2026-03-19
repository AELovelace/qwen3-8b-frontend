# path\_exists

This function returns whether a path with the given index exists or not.

Note that if you check for the existence of a path through a variable that has yet to have been declared, this will throw an error.

 

#### Syntax:

path\_exists(index)

 

| Argument | Type | Description |
| --- | --- | --- |
| index | [Path Asset](../../../../../The_Asset_Editors/Paths.md) | The index of the path to check for. |

 

#### Returns:

[Boolean](../../../../GML_Overview/Data_Types.md)

 

#### Example:

if (path\_exists(my\_path))  

 {  

     path\_delete(my\_path);  

 }

This code checks to see if the given variable stores a path index and if it does, then the path is deleted from memory.
