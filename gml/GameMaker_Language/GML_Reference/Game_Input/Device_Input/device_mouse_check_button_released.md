# device\_mouse\_check\_button\_released

This function returns true or false depending on whether the device touch that you specify has been released or not.

The device argument refers to the device touch number, which can be from 0 to n, and note that the maximum number of touches that can be detected will depend very much on the device being used and the OS it runs (most devices will support at least 4 simultaneous touches).

This function only returns true once by the actual releasing action, during the step the key changed from pressed to not pressed, and the constants listed [on this page](../Mouse_Input/Mouse_Input.md) can be used to check for the mouse buttons. During all other steps, the function returns false.

  mb\_right will only have been detected if a double tap touch is detected and held on the second tap before release (this behaviour can be disabled using the function [device\_mouse\_dbclick\_enable](device_mouse_dbclick_enable.md)).

 
 

#### Syntax:

device\_mouse\_check\_button\_released(device, button)

| Argument | Type | Description |
| --- | --- | --- |
| device | [Real](../../../GML_Overview/Data_Types.md) | The device (from 0 \- *n*) that is being checked. |
| button | [Mouse Button Constant](../Mouse_Input/mouse_check_button.md) | The button of the device that is being checked. |

 

#### Returns:

[Boolean](../../../GML_Overview/Data_Types.md)

 

#### Example:

if device\_mouse\_check\_button\_released(0, mb\_left)  

 {  

     press \= false;  

 }

The above code checks to see if the device has been pressed and sets a variable to false if it has.
