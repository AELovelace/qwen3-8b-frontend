# GM\_is\_sandboxed

This boolean constant holds true when the game is running sandboxed or false when it isn't. Its value is determined by [the Compiler](../../../Introduction/Compiling.md) at compile time.

When your game is running sandboxed (the default), the writable area on the file system is limited to the **Save Area**. See [The File System](../../../Additional_Information/The_File_System.md) for more information on the sandbox.

 
 

#### Syntax:

GM\_is\_sandboxed

 

#### Returns:

[Boolean](../../GML_Overview/Data_Types.md)

 

#### Example:

draw\_text(5, 5, $"Running sandboxed: {(GM\_is\_sandboxed ? "yes" : "no")}");

The code above displays text in the top\-left corner of the room indicating if the game is running sandboxed.
