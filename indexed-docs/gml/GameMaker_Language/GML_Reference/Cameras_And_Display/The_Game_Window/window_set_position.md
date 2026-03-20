# window\_set\_position

With this function you can set the game window to a specific position within the display (on macOS, Ubuntu and Windows) or within the browser (HTML5\).

 Calling this function on the same frame as a call to [window\_set\_size](window_set_size.md) might make it fail to set the window position correctly. Call this function in a different frame (e.g. by setting an alarm for a few frames later to set the position of the window) to prevent issues.

 If your HTML5 game uses a custom index.html and that sets the canvas to a fixed position then this function will have no effect on the window position.

 

#### Syntax:

window\_set\_position(x, y)

| Argument | Type | Description |
| --- | --- | --- |
| x | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate of where to position the window. |
| y | [Real](../../../GML_Overview/Data_Types.md) | The y coordinate of where to position the window. |

 

#### Returns:

N/A

 

#### Example:

window\_set\_position(0, 0\);

The above code will position the game window in the upper left corner of the browser or display (depending on the target module being used).
