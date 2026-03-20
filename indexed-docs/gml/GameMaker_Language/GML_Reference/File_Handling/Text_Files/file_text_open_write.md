# file\_text\_open\_write

This function opens the text file with the indicated filename for *writing only* (if the file does not exist, it is created), returning the unique *id* of the file that which should be stored in a variable as it will be used for all further actions to do with that file.

 

If the file already exists, using this function will cause it to be overwritten when data is saved. If you want to add data to a file while keeping its existing contents intact, use [file\_text\_open\_append()](file_text_open_append.md).

  You can only have a maximum of 32 files open at any one time. You should also **always** close files when finished as this writes the information and frees the memory associated with the file.

 
 

#### Syntax:

file\_text\_open\_write(fname)

| Argument | Type | Description |
| --- | --- | --- |
| fname | [String](../../../GML_Overview/Data_Types.md) | The name of the file to write to. |

 

#### Returns:

[Text File ID](file_text_open_read.md) or \-1

 

#### Example:

var file;  

 file \= file\_text\_open\_write(working\_directory \+ "level.txt");  

 file\_text\_write\_string(file, level\_data);  

 file\_text\_close(file);

The above code will open the file "level.txt" for writing and then write the string stored in the variable "level\_data" before finally closing the file again.
