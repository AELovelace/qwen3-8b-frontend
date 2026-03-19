# device\_mouse\_check\_button\_pressed

This function returns true or false depending on whether the device that you specify has been "touched" (clicked) or not.

The device argument refers to the touch number, which can be from 0 to n, and the maximum number of touches that can be detected will depend very much on the device being used and the OS it runs (most devices will support at least 4 simultaneous touches).

This function only returns true *once* by the actual pressing action, during the step the key changed from not pressed to pressed, and the constants listed [on this page](../Mouse_Input/Mouse_Input.md) can be used to check for the mouse buttons. During all other steps, the function returns false.

  mb\_right will only be detected if a double tap touch is detected and held on the second tap (this behaviour can be disabled using the function [device\_mouse\_dbclick\_enable](device_mouse_dbclick_enable.md)).

 
 

#### Syntax:

device\_mouse\_check\_button\_pressed(device, button)

| Argument | Type | Description |
| --- | --- | --- |
| device | [Real](../../../GML_Overview/Data_Types.md) | The device (from 0 \- *n*) that is being checked. |
| button | [Mouse Button Constant](../Mouse_Input/mouse_check_button.md) | The button of the device that is being checked. |

 

#### Returns:

[Boolean](../../../GML_Overview/Data_Types.md)

 

#### Example:

if device\_mouse\_check\_button\_pressed(0, mb\_left)  

 {  

     press \= true;  

 }

The above code checks to see if the device has been pressed and sets a variable to true if it has.
