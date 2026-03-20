# file\_bin\_open

This function will open the binary file with the indicated name. The mode indicates what can be done with the file:

- 0 \= reading
- 1 \= writing
- 2 \= both reading and writing

When the file does not exist it is created, and the function returns the id of the file that must be used in the other functions. You can open multiple files at the same time (32 max), but don't forget to close them once you are finished with them.

In the case of an error, the function will return \-1\. However, in some cases where the file could not be loaded (like an invalid filename being passed), the function may still return a file ID, in which case the return value of the [file closing](file_bin_close.md) function will be false.

 
These functions **do not** work when the target module is HTML5\.

 

#### Syntax:

file\_bin\_open(fname, mode)

| Argument | Type | Description |
| --- | --- | --- |
| fname | [String](../../../GML_Overview/Data_Types.md) | The name of the file to read from. |
| mode | [Real](../../../GML_Overview/Data_Types.md) | The indicator of what can be done with the file. |

 

#### Returns:

[Binary File ID](file_bin_open.md) or \-1

 

#### Example:

file \= file\_bin\_open("myfile.bin", 2\);

This would open a file from the same directory as the game, and assign its index to the variable "file".
