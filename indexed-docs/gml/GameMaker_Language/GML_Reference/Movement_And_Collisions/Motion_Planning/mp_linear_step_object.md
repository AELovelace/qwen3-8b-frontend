# mp\_linear\_step\_object

With this function you tell an instance to take a "step" towards the given target position. The instance may stop at a collision with instances of a given object, with a single instance or with [all](../../../GML_Overview/Instance Keywords/all.md) instances.

The size of the step (which is how many pixels the instance should move each step) is indicated by the step size, and if the instance is already at the position it will stop and not move any further, contrary to other, simpler functions like [move\_towards\_point](../Movement/move_towards_point.md). The step size is also the distance "ahead" that the object will check each step for a collision, and you can choose whether the instance stops at a collision with an object or instance of your choice.

 

#### Syntax:

mp\_linear\_step\_object(xgoal, ygoal, stepsize, obj)

| Argument | Type | Description |
| --- | --- | --- |
| xgoal | [Real](../../../GML_Overview/Data_Types.md) | The target x position |
| ygoal | [Real](../../../GML_Overview/Data_Types.md) | The target y position |
| stepsize | [Real](../../../GML_Overview/Data_Types.md) | The speed the instance moves in pixels per step |
| obj | [Object Asset](../../../../The_Asset_Editors/Objects.md) or [Object Instance](../../Asset_Management/Instances/Instance_Variables/id.md) | The object that is to block the path. Can be an object index, an instance id or the special keyword [all](../../../GML_Overview/Instance Keywords/all.md) |

 

#### Returns:

[Boolean](../../../GML_Overview/Data_Types.md)

 

#### Example:

if (mp\_linear\_step\_object(mouse\_x, mouse\_y, 5, obj\_wall))  

 {  

     instance\_create\_layer(x, y, "Effects", obj\_explosion);  

     instance\_destroy();  

 }

The above code will make the object move towards the mouse at a speed of 5 pixels per step, only checking for collisions with instances of obj\_wall. Once it reaches the mouse position it will create an instance of obj\_explosion and destroy itself.
