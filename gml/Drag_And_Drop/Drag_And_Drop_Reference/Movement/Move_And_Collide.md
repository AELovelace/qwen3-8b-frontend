# Move And Collide

This action moves the instance by the given distance on the X and Y axes, while avoiding the given object(s).

It allows your instance to move while navigating slopes or small steps that would otherwise prevent it from being able to move.

The "Iterations" argument is the number of steps it takes to get to the target position. Collisions with the given object are checked after each step.

For more details on how this works, see the GML Code version: [move\_and\_collide](../../../GameMaker_Language/GML_Reference/Movement_And_Collisions/Movement/move_and_collide.md).

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Object | The object or instance ID to avoid (such as a wall object). You can click the  icon to add multiple objects to check collisions with. |
| X Dist | The number of pixels to move on the X axis (horizontally) |
| Y Dist | The number of pixels to move on the Y axis (horizontally) |
| Iterations | The number of steps to take to get to the target position (default is 4\) |
| X Offset | The x component of the direction in which to move in case of a collision; specify 0 to use the default behaviour (perpendicular direction of movement) |
| Y Offset | The y component of the direction in which to move in case of a collision; specify 0 to use the default behaviour (perpendicular direction of movement) |
| Max X Movement | The maximum speed the instance should move on the X axis; specify \-1 for no limit |
| Max Y Movement | The maximum speed the instance should move on the Y axis; specify \-1 for no limit |

 

#### Example:

This checks if the left arrow key is held, and in that case it moves the instance left by 2 pixels while checking for collisions with obj\_wall.
