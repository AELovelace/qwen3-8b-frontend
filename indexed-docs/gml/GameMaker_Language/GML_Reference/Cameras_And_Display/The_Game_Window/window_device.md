# window\_device

This function will return the current d3d device *pointer*, which you can then (for example) pass through to a DLL or Dylib on Windows and macOS.

NOTE This function has been deprecated in GameMaker in favour of [os\_get\_info()](../../OS_And_Compiler/os_get_info.md).

 

#### Syntax:

window\_device()

 

#### Returns:

[Pointer](../../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

gfx\_pointer \= window\_device();

The above code will store the d3d device pointer in a variable.
