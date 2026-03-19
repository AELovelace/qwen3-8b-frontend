# mp\_linear\_path

This function computes a straight line path from the current instance position to the given target position. The path may be blocked by all instances or just solid ones.

It uses the indicated step size, the same as in the function [mp\_linear\_step](mp_linear_step.md). The indicated path must already exist and will be overwritten by the new path and the function will return if a complete path was found (true) or not (false). If false is returned then a path is still generated, but it will only run up to the position where the path was blocked.

  This function does not move the instance. It sets a path only, and you must use the [Path](../../Asset_Management/Paths/Paths.md) functions for movement.

 

#### Syntax:

mp\_linear\_path(path, xgoal, ygoal, stepsize, checkall)

| Argument | Type | Description |
| --- | --- | --- |
| path | [Path Asset](../../../../The_Asset_Editors/Paths.md) | The path to be used |
| xgoal | [Real](../../../GML_Overview/Data_Types.md) | The target x position |
| ygoal | [Real](../../../GML_Overview/Data_Types.md) | The target y position |
| stepsize | [Real](../../../GML_Overview/Data_Types.md) | The speed the instance moves in pixels per step |
| checkall | [Boolean](../../../GML_Overview/Data_Types.md) | Whether to check for collisions with all instances (true) or just solid ones (false) |

 

#### Returns:

[Boolean](../../../GML_Overview/Data_Types.md)

 

#### Example:

if (mp\_linear\_path(path, obj\_player.x, obj\_player.y, 2, 0\))  

 {  

     path\_start(path, 2, 0, 0\);  

 }

This gets the object to check and see if there is a linear path from its current position to the position of the instance of obj\_player. If there is then it starts the path.
