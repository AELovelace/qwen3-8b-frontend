# file\_text\_open\_append

This function opens the text file with the indicated filename for *writing* (if the file does not exist, it is created), returning the unique *id* of the file that which should be stored in a variable as it will be used for all further actions to do with that file. The position within the file for writing to is set to the last line of text that the file contains, so any existing data is not overwritten.

 

You can only have a maximum of 32 files open at any one time. You should also **always** close files when finished as this writes the information and frees the memory associated with the file.

 
 

#### Syntax:

file\_text\_open\_append(fname)

| Argument | Type | Description |
| --- | --- | --- |
| fname | [String](../../../GML_Overview/Data_Types.md) | The name of the file to append to. |

 

#### Returns:

[Text File ID](file_text_open_read.md) or \-1

 

#### Example:

file \= file\_text\_open\_append(working\_directory \+ "save.txt");

This would open "save.txt" from the same directory as the game and store the file id in the variable "file".
