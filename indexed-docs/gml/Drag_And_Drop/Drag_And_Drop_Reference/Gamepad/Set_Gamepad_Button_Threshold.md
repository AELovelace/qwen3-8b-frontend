# Set Gamepad Button Threshold

This action can be used to set the "threshold" of the gamepad analogue buttons. You specify the gamepad index to set, and then set a value from 0 to 1 and if the analogue button input amount is lower than the given value, the gamepad button is considered to be at 0\. Note that this is a *global* setting that will affect *all* analogue buttons connected gamepad. This value will be used in all [down](If_Gamepad_Button_Down.md), [pressed](If_Gamepad_Button_Pressed.md) and [released](If_Gamepad_Button_Released.md) checks for the given gamepad, but will be *ignored* by the action [Get Gamepad Trigger](Get_Gamepad_Trigger.md).

 

#### Action Syntax:

 

#### Arguments:

| Argument | Description |
| --- | --- |
| Gamepad | The gamepad index. |
| Deadzone | The threshold value (0 \- 1\) |

 

#### Example:

  

 The above action block code sets the button threshold for all gamepad indices to 0\.2\.
