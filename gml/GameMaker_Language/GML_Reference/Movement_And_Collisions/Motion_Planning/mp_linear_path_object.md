# mp\_linear\_path\_object

This function computes a straight line path from the current instance position to the given target position. The path may be blocked by instances of a given object, by a single instance or by [all](../../../GML_Overview/Instance Keywords/all.md) instances.

The function uses the given step size, the same as in the function [mp\_linear\_step](mp_linear_step.md). The indicated path must already exist and will be overwritten by the new path and the function will return if a complete path was found (true) or not (false). A full path is only found if there was no collision with the specified object or instance, and if false is returned, a path is still generated, but it will only run up to the position where the path was blocked.

  This function does not move the instance. It sets a path only, and you must use the [Path](../../Asset_Management/Paths/Paths.md) functions for movement.

 

#### Syntax:

mp\_linear\_path\_object(path, xgoal, ygoal, stepsize, obj)

| Argument | Type | Description |
| --- | --- | --- |
| path | [Path Asset](../../../../The_Asset_Editors/Paths.md) | The path to be used |
| xgoal | [Real](../../../GML_Overview/Data_Types.md) | The target x position |
| ygoal | [Real](../../../GML_Overview/Data_Types.md) | The target y position |
| stepsize | [Real](../../../GML_Overview/Data_Types.md) | The speed the instance moves in pixels per step |
| obj | [Object Asset](../../../../The_Asset_Editors/Objects.md) or [Object Instance](../../Asset_Management/Instances/Instance_Variables/id.md) | The object that is to block the path. Can be an object index, an instance id or the special keyword [all](../../../GML_Overview/Instance Keywords/all.md) |

 

#### Returns:

[Boolean](../../../GML_Overview/Data_Types.md)

 

#### Example:

if (mp\_linear\_path\_object(path, mouse\_x, mouse\_y, 4, obj\_wall))  

 {  

     path\_start(path, 4, 0, 0\);  

 }

The above code checks for a collision with obj\_wall along the path between the object running the code and the x/y position of the mouse. If there is no collision and the complete path is generated then it will start the object along the path generated.
