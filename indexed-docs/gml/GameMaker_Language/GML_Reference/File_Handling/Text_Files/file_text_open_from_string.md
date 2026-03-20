# file\_text\_open\_from\_string

This function will create a text file from a string and open it for reading, returning the file "handle" that should be used in all further file function calls to read from this file. Note that this file is temporary and *read only*, and as such it will be removed from memory the moment it is closed.

 

You can only have a maximum of 32 files open at any one time. You should also **always** close files when finished as this writes the information and frees the memory associated with the file.

 
 

#### Syntax:

file\_text\_open\_from\_string(string)

| Argument | Type | Description |
| --- | --- | --- |
| string | [String](../../../GML_Overview/Data_Types.md) | The string to create the file from. |

 

#### Returns:

[Text File ID](file_text_open_read.md) or \-1

 

#### Example:

file \= file\_text\_open\_from\_string(reset\_str);

The above code takes the string stored in the variable "reset\_str" and uses it to create a read\-only text file. The "handle" for this file is then stored in the variable "file" for all further file functions to use.
