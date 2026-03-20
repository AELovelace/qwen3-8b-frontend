# window\_handle

With this function you can get the internal Windows ID value (the HWND, a *pointer*).

This function is really only useful for extension writers who need the **window handle** to call Windows API's in DLL code (the returned pointer should be cast into a string and then in the C\+\+ just cast it to an HWND). The table below shows the platforms supported along with what they return:

| Platform | Returns |
| --- | --- |
| Windows | Window HWND |
| macOS | NSWindow class |
| Ubuntu (Linux) | XWindow handle |
| HTML5 | Canvas ID |
| GX.games | Name of canvas element |

 

#### Syntax:

window\_handle()

 

#### Returns:

[Pointer](../../../GML_Overview/Data_Types.md)

 

#### Example:

win\_id \= windows\_handle();

The above code will store the game window ID in a variable.
