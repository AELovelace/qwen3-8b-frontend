# file\_attributes

You can use this function to check if the given file has all the attributes that you specify.

You can add up the following constants to check the type of files you want:

| Constant | Description |
| --- | --- |
| fa\_readonly | Read\-only files |
| fa\_hidden | Hidden files |
| fa\_sysfile | System files |
| fa\_volumeid | Volume\-id files |
| fa\_directory | Directories |
| fa\_archive | Archived files |

This is a Windows only function.

 

#### Syntax:

file\_attributes(fname, attr)

| Argument | Type | Description |
| --- | --- | --- |
| fname | [String](../../../GML_Overview/Data_Types.md) | The name of the file to check |
| attr | [File Attribute Constant](file_find_first.md) | The attributes to check for |

 

#### Returns:

[Boolean](../../../GML_Overview/Data_Types.md)

 

#### Example:

if (!file\_attributes(file, fa\_hidden))  

 {  

     file\_delete(file);  

 }

This would check a file to see if it is hidden or not, and if not it is deleted.
