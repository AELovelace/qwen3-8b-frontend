# file\_bin\_position

This function will returns the current position in bytes, where 0 is the first position, of the file with the given file id. You supply the file ID value, as returned by the function [file\_bin\_open()](file_bin_open.md).

**NOTE**: These functions **do not** work when the target module is HTML5\.

 

#### Syntax:

file\_bin\_position(binfile)

| Argument | Type | Description |
| --- | --- | --- |
| binfile |  | The ID of the file to get the position in. |

 

#### Returns:

 

#### Example:

pos \= file\_bin\_position(file);

This would store the current position in the variable "pos".
