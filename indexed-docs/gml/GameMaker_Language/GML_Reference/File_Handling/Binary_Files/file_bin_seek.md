# file\_bin\_seek

This function moves the current read position within the file to the indicated position. You supply the file ID value, as returned by the function [file\_bin\_open()](file_bin_open.md), and to append a file, move the position to the
 size of the file before writing.

**NOTE**: These functions **do not** work when the target module is HTML5\.

 

#### Syntax:

file\_bin\_seek(binfile, pos)

| Argument | Type | Description |
| --- | --- | --- |
| binfile |  | The ID of the file to read from. |
| pos |  | The position in the file to move to. |

 

#### Returns:

 

#### Example:

file \= file\_bin\_open("myfile.bin", 2\);  
 size \= file\_bin\_size(file);  
 file\_bin\_seek(file, size);

This would open a file from the same directory as the game, and assign its index to the variable "file", then get the size of the file and set the next writing position to that size.
