# path\_start

This function tells the calling instance to start the given path. The path started by the instance is stored in the variable [path\_index](Path_Variables/path_index.md).

 
A path is created from a series of defining points that are linked together and then used to plan the movements of an instance. They can be created with code, *or* in [The Path Editor](../../../../The_Asset_Editors/Paths.md) and they are assigned to an instance to use in the game. You would then use this function to tell your instance which path to follow, what speed to follow the path (measured in pixels per step), how to behave when it reaches the end of the path, and whether to follow the *absolute* or *relative* path position. This last part means that it either starts and follows the path exactly as you designed and placed it in [The Path Editor](../../../../The_Asset_Editors/Paths.md) (absolute), or it starts and follows the path from the position at which the instance was created (relative).

As you can see in the above image, the two instances are following the same path started with path\_start, but one of the instances is following the absolute path while the other is following the relative path. It should be noted that when absolute is set to false (i.e. relative) the instance will "jump" to the start of the path no matter where in the room it is placed.

The constants used to define the behaviour of the instance when it reaches the end of the path are given [on this page](Path_Variables/path_endaction.md).

  When following a path, an instance's position is updated [after the Step event](../../../../The_Asset_Editors/Object_Properties/Event_Order.md), so during the Step event its [x](../Instances/Instance_Variables/x.md) and [y](../Instances/Instance_Variables/y.md) position will be the same as its [xprevious](../Instances/Instance_Variables/xprevious.md) and [yprevious](../Instances/Instance_Variables/yprevious.md) (unless manually modified in the Begin Step or Step events).

 

#### Syntax:

path\_start(path, speed, endaction, absolute)

| Argument | Type | Description |
| --- | --- | --- |
| path | [Path Asset](../../../../The_Asset_Editors/Paths.md) | The path index to start. |
| speed | [Real](../../../GML_Overview/Data_Types.md) | The speed of which to follow the path in pixels per step, negative meaning going backwards. |
| endaction | [Path End Action Constant](Path_Variables/path_endaction.md) | What to do when the end of the path is reached. |
| absolute | [Boolean](../../../GML_Overview/Data_Types.md) | Whether the calling instance should follow the absolute path as it is defined in [The Path Editor](../../../../The_Asset_Editors/Paths.md) (true) or a relative path to its current position (false). |

 

#### Returns:

N/A

 

#### Example:

path\_start(path, 4, path\_action\_reverse, false);

This will make the calling instance follow the path indexed in the variable "path" at a speed of 4 pixels per step. It will follow the path relative to its own position, and when it reaches the end it will reverse direction and go back the way it came.
