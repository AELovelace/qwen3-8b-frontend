# window\_mouse\_set

With this function you can change or set the position of the mouse within the game window. The function will only work while the game is in focus and using alt \+ tab will unlock the mouse.

  This function can only be used on the desktop platforms (**Windows**, **Ubuntu** and **macOS**).

  For regular mouse functions see the section on [Mouse Input](../../Game_Input/Mouse_Input/Mouse_Input.md).

 
   You can lock the mouse within the window by calling [window\_mouse\_set\_locked](window_mouse_set_locked.md) which removes the need to set the mouse position manually.

 

#### Syntax:

window\_mouse\_set(x, y)

| Argument | Type | Description |
| --- | --- | --- |
| x | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate in the window. |
| y | [Real](../../../GML_Overview/Data_Types.md) | The y coordinate in the window. |

 

#### Returns:

N/A

 

#### Example:

window\_mouse\_set(window\_get\_width() / 2, window\_get\_height() / 2\);

The above code centers the mouse in the game window.
