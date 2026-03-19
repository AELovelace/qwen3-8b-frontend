# file\_bin\_read\_byte

This function will return a byte of data from current position within the file with the given file ID. You supply the file ID value, as returned by the function [file\_bin\_open()](file_bin_open.md).

**NOTE**: These functions **do not** work when the target module is HTML5\.

 

#### Syntax:

file\_bin\_read\_byte(binfile)

| Argument | Type | Description |
| --- | --- | --- |
| binfile |  | The ID of the file to get the data from. |

 

#### Returns:

 

#### Example:

file \= file\_bin\_open("myfile.bin", 2\);  
 data \= file\_bin\_read\_byte(file);  
 file\_bin\_close(file);
 

This would open a file from the same directory as the game, and get a byte of data from it before closing it again.
