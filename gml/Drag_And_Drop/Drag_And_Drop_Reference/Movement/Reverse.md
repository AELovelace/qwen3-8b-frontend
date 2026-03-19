# Reverse

This action is used to reverse certain values related to direction and movement. The available options are:

Reversing *direction* will simply add 180° to the current direction (looping around 360° if necessary, so, for example, reversing 270° would give you 90°), reversing the *horizontal* or *vertical* speed will simply multiply the given speed vector by \-1, and choosing *gravity* will do the same as choosing direction, only for the gravity direction.

 

#### Action Syntax:

#### Arguments:

 

| Argument | Description |
| --- | --- |
| direction | The direction to reverse |

 

#### Example:

The above action block code checks for a collision of the instance with "obj\_Wall" relative to the current position to the left and to the right. If one is found then the horizontal speed is reversed. It then does the same for above and below the instance, reversing the vertical speed if a collision is detected.
