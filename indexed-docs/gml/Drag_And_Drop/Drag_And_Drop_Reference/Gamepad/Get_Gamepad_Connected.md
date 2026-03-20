# Get Gamepad Connected

You can use this action to check and see if a given gamepad "slot" has a gamepad connected. You supply the gamepad index (this is the number of "slot" that a gamepad occupies) and the returned value will be stored in the target variable
 that you supply for future use (this can be flagged as a temporary local variable that you create for this event or script).

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Gamepad | The gamepad index to check. |
| Target | The target variable to store the returned value in. |

 

#### Example:

The above action block code runs a for loop to check and see if a gamepad
 is connected to any of the 12 available "slots". If a gamepad is discovered, a global variable is set to the current slot number and the loop is broken.
