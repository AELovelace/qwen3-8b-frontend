# file\_bin\_write\_byte

This function will write a byte of data to the file identified by the file ID at the current write position. You supply the file ID value, as returned by the function [file\_bin\_open()](file_bin_open.md) and the byte of data to write.

**NOTE**: These functions **do not** work when the target module is HTML5\.

 

#### Syntax:

file\_bin\_write\_byte(binfile, byte)

| Argument | Type | Description |
| --- | --- | --- |
| binfile |  | The ID of the file to write to. |
| byte |  | The data to write. |

 

#### Returns:

 

#### Example:

file\_bin\_write\_byte(file, data);

This would write a byte to the selected file.
