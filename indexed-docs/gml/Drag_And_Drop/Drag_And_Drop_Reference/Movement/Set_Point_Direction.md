# Set Point Direction

This action is used to set a direction from a vector formed by the current position of the instance and the position given. You supply the x and y position to "point" at \- these can be flagged as relative to the instance position \- and the direction from the instance to that point will be used for the instance.

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| x | The x component of the direction vector. |
| y | The y component of the direction vector. |

 

#### Example:

The above action block code checks checks to see if an instance of the object "obj\_Player" exists in the room and if it does it then sets the direction of the instance to point towards the x/y position of "obj\_Player".
