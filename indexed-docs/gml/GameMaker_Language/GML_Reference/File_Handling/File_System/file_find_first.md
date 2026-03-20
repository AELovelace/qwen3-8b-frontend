# file\_find\_first

This function returns the name of the first file that satisfies the mask and attributes, or an empty string "" if no such file exists.

The mask can contain a path with wildcards, for example C:/temp/\*.doc.

The attributes give the additional files you want to see, so the normal files are always returned when they satisfy the mask. You can add up the following constants to see the type of files you want (using \|). If you do not wish to add any attributes, use 0 or fa\_none.

| [File Attribute Constant](file_find_first.md) | |
| --- | --- |
| Constant | Description |
| fa\_none | No file attributes |
| fa\_readonly | Read\-only files |
| fa\_hidden | Hidden files |
| fa\_sysfile | System files |
| fa\_volumeid | Volume\-id files |
| fa\_directory | Directories |
| fa\_archive | Archived files |

Attributes can only be used on Windows. For all other platforms, use 0 or fa\_none.

 
 
 

#### Syntax:

file\_find\_first(mask, attr)

| Argument | Type | Description |
| --- | --- | --- |
| mask | [String](../../../GML_Overview/Data_Types.md) | The mask to use for searching |
| attr | [File Attribute Constant](file_find_first.md)(s) | The specific file attribute(s) to look for |

 

#### Returns:

[String](../../../GML_Overview/Data_Types.md)

 

#### Example:

if (directory\_exists("/User Content"))  

 {  

     fileA \= file\_find\_first("/User Content/\*.doc", fa\_readonly);  

     fileB \= file\_find\_next();  

     fileC \= file\_find\_next();  

     file\_find\_close();  

 }

This code checks if the specified directory exists and if it does, goes there and returns the first "read\-only" .doc file found. It then looks for two more files and closes the file finder.

You can look for any number of files using a [while](../../../GML_Overview/Language_Features/while.md) loop:

var \_files \= \[];  

 var \_file\_name \= file\_find\_first("/User Content/\*.doc", fa\_readonly);  

  

 while (\_file\_name !\= "")  

 {  

     array\_push(\_files, \_file\_name);  

  

     \_file\_name \= file\_find\_next();  

 }  

  

 file\_find\_close();
 

The above code creates an empty array to store all the file names that were found, and starts looking for read\-only .doc files. If that file name is not an empty string, it pushes it into the \_files array, and then attempts to find the next file. The loop will keep repeating until an empty string is returned (meaning there are no more matching files), which is when it ends the loop and closes the file finder at the end.
