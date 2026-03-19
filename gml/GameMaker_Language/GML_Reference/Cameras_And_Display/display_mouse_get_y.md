# display\_mouse\_get\_y

This function will return the mouse y position within the *screen*. It should be noted that this function only works properly when used on the Windows and macOS targets.

It can be used for HTML5 too, but will only return a value *relative* to the 0,0 of the canvas itself, and will not return any value while the mouse is outside of the canvas.

For other devices it will return 0, and you should use the [device\_mouse\_raw\_x()](../Game_Input/Device_Input/device_mouse_raw_x.md) and [device\_mouse\_raw\_y()](../Game_Input/Device_Input/device_mouse_raw_y.md) functions instead.

 

#### Syntax:

display\_mouse\_get\_y()

 

#### Returns:

[Real](../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

my\_y \= display\_mouse\_get\_y();

This would set my\_y to the y coordinate of the mouse relative to the display.
