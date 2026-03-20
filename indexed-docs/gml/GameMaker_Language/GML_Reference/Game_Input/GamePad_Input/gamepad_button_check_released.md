# gamepad\_button\_check\_released

This function will return true or false depending on whether the given gamepad button is detected as having been released or not. Note that this function will only trigger *once* for the button the moment it has been released. For it to trigger again the button must first be pressed and then released once more. If you are checking an analogue button, then the check will take into consideration the [threshold setting](gamepad_set_button_threshold.md) and only return true when the raw input value goes under the given threshold (you can get this raw value using the function [gamepad\_button\_value()](gamepad_button_value.md)).

 

#### Syntax:

gamepad\_button\_check\_released(device, button)

| Argument | Type | Description |
| --- | --- | --- |
| device | [Real](../../../GML_Overview/Data_Types.md) | Which gamepad device "slot" to check. |
| button | [Gamepad Button Constant](Gamepad_Input.md) | Which gamepad button [constant](Gamepad_Input.md) to check for. |

 

#### Returns:

[Boolean](../../../GML_Overview/Data_Types.md)

 

#### Example:

if (gamepad\_button\_check\_released(0, gp\_select))  

 {  

     audio\_play\_sound(snd\_Button, 0, false);  

     global.Pause \= !global.Pause;  

 }

The above code will detect whether the "select" button of the gamepad connected to device "slot" 0 has been pressed or not and toggle the global "Pause" variable.
