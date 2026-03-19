# Set Gamepad Axis Deadzone

This action can be used to set the "dead zone" of the gamepad stick axis. You specify the gamepad index to set, and then set a value from 0 to 1 and if the input amount is lower than the given value, the gamepad stick axis is considered to be at 0\. Note that this is a global setting that will affect *all* axis of the stick connected.

Note that this does not modify the output of the [Get Gamepad Axis](Get_Gamepad_Axis.md) action, which will always return a value from \-1 and 0, and 0 and 1\. For example, setting the deadzone to 0\.2 will mean that pushing the stick right will only start returning a value from 0 \- 1 when the *raw* axis value is over 0\.2 \- so when the raw value is 0\.2, the return value will be 0, when the raw value is at 0\.5, the return value will be 0\.375, or if the raw value is 0\.9, then the return value would be 0\.875\.

 

#### Action Syntax:

 

#### Arguments:

| Argument | Description |
| --- | --- |
| Gamepad | The gamepad index. |
| Deadzone | The deadzone value (0 \- 1\) |

 

#### Example:

The above action block code sets the deadzone for all gamepad indices to 0\.2\.
