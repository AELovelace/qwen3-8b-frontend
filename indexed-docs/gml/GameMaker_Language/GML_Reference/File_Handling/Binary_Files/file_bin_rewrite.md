# file\_bin\_rewrite

This function takes the filename handle as returned by the function [file\_bin\_open()](file_bin_open.md) and then rewrites the file, clearing it of all previous data to start writing from the beginning of the file.

**NOTE**: These functions **do not** work when the target module is HTML5\.

 

#### Syntax:

file\_bin\_rewrite(binfile)

| Argument | Type | Description |
| --- | --- | --- |
| binfile |  | The ID of the file to rewrite. |

 

#### Returns:

 

#### Example:

file \= file\_bin\_open("myfile.bin", 2\);  
 file\_bin\_rewrite(file);
 

This would open a file from the same directory as the game, and assign its index to the variable "file". It would then re\-write the file (clearing it of data).
