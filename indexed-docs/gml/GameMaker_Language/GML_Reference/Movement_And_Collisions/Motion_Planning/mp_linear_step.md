# mp\_linear\_step

With this function you tell an instance to take a "step" towards the given target position. The instance may stop at a collision with all instances or just solid ones.

The size of the step (which is how many pixels the instance should move each step) is indicated by the step size, and if the instance is already at the position it will stop and not move any further, contrary to other, simpler functions like [move\_towards\_point](../Movement/move_towards_point.md). The step size is also the distance "ahead" that the object will check each step for a collision, and you can choose whether the instance stops at a collision with *any* instance or only those that are flagged as solid. The function will return whether it has reached the goal position (true) or if it has failed (false).

  This function does not try to make detours if it meets an obstacle, it simply fails and stops moving.

 

#### Syntax:

mp\_linear\_step(xgoal, ygoal, stepsize, checkall)

| Argument | Type | Description |
| --- | --- | --- |
| xgoal | [Real](../../../GML_Overview/Data_Types.md) | The target x position |
| ygoal | [Real](../../../GML_Overview/Data_Types.md) | The target y position |
| stepsize | [Real](../../../GML_Overview/Data_Types.md) | The speed the instance moves in pixels per step |
| checkall | [Boolean](../../../GML_Overview/Data_Types.md) | Whether to check all instances (true) or just solid ones (false) |

 

#### Returns:

[Boolean](../../../GML_Overview/Data_Types.md)

 

#### Example:

if (mp\_linear\_step(mouse\_x, mouse\_y, 5, 0\))  

 {  

     instance\_create\_layer(x, y, "Effects", obj\_explosion);  

     instance\_destroy();  

 }

The above code will make the object move towards the mouse at a speed of 5 pixels per step. Once it reaches the mouse position it will create an object obj\_explosion and destroy itself.
