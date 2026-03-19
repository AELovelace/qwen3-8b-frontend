# room\_instance\_add

This function adds an instance to any room other than the current one at any position within that room.

The function returns the unique [id](../Instances/Instance_Variables/id.md) of the instance which can then be used in further function calls to set properties, etc. of that instance, but **only once the game has entered the specified room**. If you wish to create an instance in the current room you should be using the function [instance\_create\_layer](../Instances/instance_create_layer.md).

  Calling this function on a room asset created in [The Asset Browser](../../../../Introduction/The_Asset_Browser.md) **will permanently add the instance to the room**, and even calling [game\_restart](../../General_Game_Control/game_restart.md) will not return the room to its original state. Only ending the game and opening it again will start with the room in its original state again.

 

#### Syntax:

room\_instance\_add(index, x, y, obj)

| Argument | Type | Description |
| --- | --- | --- |
| index | [Room Asset](../../../../The_Asset_Editors/Rooms.md) | The room to add an object instance to. |
| x | [Real](../../../GML_Overview/Data_Types.md) | The x position of the new instance. |
| y | [Real](../../../GML_Overview/Data_Types.md) | The y position of the new instance. |
| obj | [Object Asset](../../../../The_Asset_Editors/Objects.md) | The object to add an instance of. |

 

#### Returns:

[Object Instance](../Instances/Instance_Variables/id.md)

 

#### Example:

global.rm \= room\_add();  

 room\_assign(rm\_base, global.rm);  

room\_instance\_add(global.rm, 100, 100, obj\_player);
 

The above code will add a new room to the game and then copy the contents of the room indexed as rm\_base into it. It will then add an instance of the object obj\_player at the position (100, 100\) of this new room.
