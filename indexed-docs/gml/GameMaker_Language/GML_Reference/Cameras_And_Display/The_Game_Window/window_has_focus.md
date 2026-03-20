# window\_has\_focus

With this function you can poll the window (or tab) state and if it loses focus the function will return false, otherwise it will return true. In most cases you can simply use the [os\_is\_paused](../../OS_And_Compiler/os_is_paused.md) function to test this, but in some very specific cases (for example games on Chrome Apps) that function will not trigger, in which case you should use this function instead.

 This function is only valid on the HTML5, GX.games, Windows, and macOS platforms.

 

#### Syntax:

window\_has\_focus()

 

#### Returns:

[Boolean](../../../GML_Overview/Data_Types.md)

 

#### Example:

if (!window\_has\_focus())  

 {  

     pause\_game();  

 }

The above code will check to see if the game window is in focus or not, and if the function returns false, a function will be called.
