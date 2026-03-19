# Get Gamepad Trigger

You can use this action to get the value of the different triggers from a given gamepad. You supply the gamepad index (this is the number of "slot" that a gamepad occupies) and select the the trigger to check (left or right). The value returned
 will be between 0 and 1, where 0 is no pressure on the trigger and 1 full pressure. This returned value will be stored in the target variable that you supply for future use. Note that this function does *not* take into account the [threshold setting](Set_Gamepad_Button_Threshold.md).

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Gamepad | The gamepad index. |
| Trigger | The trigger to check (left/right) |
| Target | The target variable to store the returned value in. |

 

#### Example:

The above action block code creates a local (temporary) variable and then uses it to store
 the current value for the left trigger. If the trigger value is over 0\.5 an instance is created at the calling instance's position.
