# file\_bin\_close

Closes a previously opened binary file. You supply the file ID value, as returned by the function [file\_bin\_open()](file_bin_open.md).

The function will return true if the operation was a success, however if there was a failure in closing the file or when the file was first [opened](file_bin_open.md), this will return false.

  These functions **do not** work when the target module is HTML5\.

 

#### Syntax:

file\_bin\_close(binfile)

| Argument | Type | Description |
| --- | --- | --- |
| binfile | [Binary File ID](file_bin_open.md) | The ID of the file to close. |

 

#### Returns:

[Boolean](../../../GML_Overview/Data_Types.md)

 

#### Example:

file \= file\_bin\_open("myfile.bin", 2\);  

 file\_bin\_rewrite(file);  

 file\_bin\_close(file);

This would open a file from the same directory as the game, and assign its index to the variable "file". It would then re\-write the file (clearing it of data), and close it again.
