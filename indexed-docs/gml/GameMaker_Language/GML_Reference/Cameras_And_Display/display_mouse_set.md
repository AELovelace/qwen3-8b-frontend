# display\_mouse\_set

With this function you can change or set the position of the mouse within the game display. The function will only work while the game is in focus and using ALT \+ Tab will unlock the mouse.

  This function is usable on the desktop platforms **Windows**, **Ubuntu** and **macOS**.

 
   You can lock the mouse within the window by calling [window\_mouse\_set\_locked](The_Game_Window/window_mouse_set_locked.md) which removes the need to set the mouse position manually.

 

#### Syntax:

display\_mouse\_set(x, y)

| Argument | Type | Description |
| --- | --- | --- |
| x | [Real](../../GML_Overview/Data_Types.md) | The x coordinate in the display. |
| y | [Real](../../GML_Overview/Data_Types.md) | The y coordinate in the display. |

 

#### Returns:

N/A

 

#### Example:

display\_mouse\_set(display\_get\_width() / 2, display\_get\_height() / 2\);

The above code centers the mouse in the game display.
