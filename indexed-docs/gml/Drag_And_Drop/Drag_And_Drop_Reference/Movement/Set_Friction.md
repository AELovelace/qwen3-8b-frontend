# Set Friction

This action is used to set the "friction" for the instance. Friction simply means that a specific amount will be deducted from the speed vector each game frame, where you specify the amount to deduct. Usually smaller values work best, like
 0\.2, but the actual amount will depend on the setup of your project. If you set the relative flag, then the amount given will be added to the current friction value instead of setting it.

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| friction | The friction to apply (positive values only) |

 

#### Example:

The above action block code sets various instance properties related to movement:
 gravity direction is set to down (270°), gravity force is set to 0\.05, and friction is set to 0\.2\.
