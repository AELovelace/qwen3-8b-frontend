# keyboard\_virtual\_set\_position

When Windows IME is enabled (see [keyboard\_virtual\_show](keyboard_virtual_show.md)) this function is used to set the position of the IME input window. This position is in the game window space, you can use [application\_get\_position](../../Drawing/Surfaces/application_get_position.md) to get the position of the application surface within the window in case the application surface is not at 0, 0.

 

#### Syntax

keyboard\_virtual\_set\_position(x, y)

| Argument | Type | Description |
| --- | --- | --- |
| x | [Real](../../../GML_Overview/Data_Types.md) | The x position in the window |
| y | [Real](../../../GML_Overview/Data_Types.md) | The y position in the window |

 

#### Returns:

N/A

 

#### Example:

var \_mx \= device\_mouse\_x\_to\_gui(0\);  

 var \_my \= device\_mouse\_y\_to\_gui(0\);  

  

 keyboard\_virtual\_show(undefined, undefined, undefined, undefined);  

 keyboard\_virtual\_set\_position(\_mx, \_my);
 

This code enables the virtual keyboard on Windows (for IME input) and sets its position to the mouse position on the GUI layer.
