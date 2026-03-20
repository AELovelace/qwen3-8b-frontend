# title

With this action you can check to see if a file with the given name exists. You select the file to check for (as a sting and including the extension) and the function will return true if it exists, and false if it does not. Note that
 this will return true if the file exists in the game bundle as an Included File or if the file has been saved out while the game was running (see the section on [The File System](../../../Additional_Information/The_File_System.md) for more information).

Note that to add actions into the "if" block, they should be dropped to the side of the action, as shown in the image below:

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Type | The type of data to read, either a string (enclosed in quotes ""), or a real number |

 

#### Example:

The above action block code will create a variable to hold buffer data and then check to see if
 a buffer save file has been made previously. If the file exists, then it is loaded into the buffer variable that we created, but if it doesn't exist, it is created, written to and then saved out ready for loading the next time.
