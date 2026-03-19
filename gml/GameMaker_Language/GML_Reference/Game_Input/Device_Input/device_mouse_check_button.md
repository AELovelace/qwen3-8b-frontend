# device\_mouse\_check\_button

This function returns true or false depending on whether the given **mouse button** is being held down on the given **device**. For the mouse button you can supply one of the constants listed [on this page](../Mouse_Input/Mouse_Input.md).

This function can be used for touch screens, and the **device** argument can be from 0 to *n* where *n* is the maximum number of "fingers" that can be touching the screen at once (the maximum number of touches that can be detected will depend very much on the device being used and the OS it runs, but most devices should detect at least up to 4\). Note that mb\_right will only be detected if a double tap touch is detected (this behaviour can be disabled using the function [device\_mouse\_dbclick\_enable](device_mouse_dbclick_enable.md)).

 
 

#### Syntax:

device\_mouse\_check\_button(device, button)

| Argument | Type | Description |
| --- | --- | --- |
| device | [Real](../../../GML_Overview/Data_Types.md) | The device (from 0 \- *n*) that is being checked |
| button | [Mouse Button Constant](../Mouse_Input/mouse_check_button.md) | The button of the device that is being checked |

 

#### Returns:

[Boolean](../../../GML_Overview/Data_Types.md)

 

#### Example:

if (device\_mouse\_check\_button(0, mb\_left) \&\& device\_mouse\_check\_button(1, mb\_left))  

 {  

     room\_goto(rm\_Menu);  

 }

The above code checks to see if the two touches are being held down at the same time and if they are then it goes to another room.
