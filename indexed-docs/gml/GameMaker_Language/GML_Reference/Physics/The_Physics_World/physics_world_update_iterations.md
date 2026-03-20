# physics\_world\_update\_iterations

This function sets the number of iterations per step that the physics system will perform.

Everything in GameMaker is based around steps and, normally, each event will only happen once per step. However, to get the necessary precision with the physics functions they are made to do several calculations each step which are called "iterations" the number of which are controlled by this function. The default number for the physics system is 10, but this can be changed to higher or lower depending how many times you want the physics to calculate each step, but it is recommended that you set this no lower than 5 and no higher than 30\. You should also be aware that this function is dependent on the [physics\_world\_update\_speed()](physics_world_update_speed.md) function.

 

#### Syntax:

physics\_world\_update\_iterations(iterations)

| Argument | Type | Description |
| --- | --- | --- |
| y1 | [Real](../../../GML_Overview/Data_Types.md) | The iterations (per step) that the physics system will perform |

 

#### Returns:

N/A

 

#### Example:

physics\_world\_update\_iterations(20\);

The code above sets the physics world in the current room to perform calculations 20 times a step.
