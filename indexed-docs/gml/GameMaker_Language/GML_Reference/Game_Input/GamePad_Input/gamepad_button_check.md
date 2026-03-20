# gamepad\_button\_check

This function will return true or false depending on whether the given gamepad button is detected as being held down or not. If you are checking an analogue button, then the check will take into consideration the [threshold setting](gamepad_set_button_threshold.md) and only return true while the raw input value is over the given threshold (you can get this raw value using the function [gamepad\_button\_value](gamepad_button_value.md)).

 

#### Syntax:

gamepad\_button\_check(device, button)

| Argument | Type | Description |
| --- | --- | --- |
| device | [Real](../../../GML_Overview/Data_Types.md) | Which gamepad device "slot" to check. |
| button | [Gamepad Button Constant](Gamepad_Input.md) | Which gamepad button [constant](Gamepad_Input.md) to check for. |

 

#### Returns:

[Boolean](../../../GML_Overview/Data_Types.md)

 

#### Example:

if gamepad\_button\_check(0, gp\_face1\)  

 {  

     if (canshoot \= true)  

     {  

         audio\_play\_sound(snd\_Shoot, 0, false);  

         instance\_create\_layer(x, y, "Bullets", obj\_Bullet)  

         canshoot \= false;  

         alarm\[0] \= game\_get\_speed(gamespeed\_fps) / 2;  

     }  

 }

The above code will detect whether the bottom button of the top face (the "X" on a PS3 controller) is being held down and if so, it will shoot a "bullet" instance and set an alarm.
