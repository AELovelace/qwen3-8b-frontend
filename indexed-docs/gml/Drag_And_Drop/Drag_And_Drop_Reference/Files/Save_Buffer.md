# title

With this action you can save a file containing the data from a buffer. You supply the unique buffer ID (as returned when you created the buffer with [Create Buffer](../Buffers/Create_Buffer.md)) and give a name for the file (as a string,
 with the extension of your choice) and the buffer will be written out to this file ready to be loaded again using [Load Buffer](Load_Buffer.md).

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Buffer | The unique buffer ID value of the buffer to save |
| Filename | The name (as a string) of the file to save |

 

#### Example:

The above action block code will create a variable to hold buffer data and then check to see if a
 buffer save file has been made previously. If the file exists, then it is loaded into the buffer variable that we created, but if it doesn't exist, it is created, written to and then saved out ready for loading the next time.
