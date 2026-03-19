# file\_copy

This function will copy the specified file, giving it the new name that you choose.

If you are copying a file on Android from within your **Included Files** area (which will be inside your APK) it will copy into memory first, so, be aware that copying very large files from the APK may cause devices to run out of memory. On the HTML5 target, we use the HTML5 **Local Storage API** for client side saving, and the functions does not support binary file operations, so assumes you are copying a text file.

The function will fail if the newname file already exists.

 
 

#### Syntax:

file\_copy(fname, newname)

| Argument | Type | Description |
| --- | --- | --- |
| fname | [String](../../../GML_Overview/Data_Types.md) | The name of the file to copy |
| newname | [String](../../../GML_Overview/Data_Types.md) | The name of the new, copied file |

 

#### Returns:

N/A

 

#### Example:

if (file\_exists("level1\.txt"))  

 {  

     file\_copy("level1\.txt", "level2\.txt");  

 }

This would check for a file and if it exists it is copied.
