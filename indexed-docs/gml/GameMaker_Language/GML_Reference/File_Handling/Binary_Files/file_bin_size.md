# file\_bin\_size

This function will return the size (in bytes) of a file that has been opened for reading and/or writing. The File ID is the value returned by the function [file\_bin\_open()](file_bin_open.md).

**NOTE**: These functions **do not** work when the target module is HTML5\.

 

#### Syntax:

file\_bin\_size(binfile)

| Argument | Type | Description |
| --- | --- | --- |
| binfile |  | The ID of the file to get the size of. |

 

#### Returns:

 

#### Example:

file \= file\_bin\_open("myfile.bin", 2\);  
 size \= file\_bin\_size(file);  
 file\_bin\_close(file);
 

This would open a file from the local directory of the game, and assign its index to the variable "file". It would then get the size of that file and close it again.
