# part\_system\_angle

This function changes the angle that the given particle system is rendered with.

 

#### Syntax:

part\_system\_angle(ind, angle)

| Argument | Type | Description |
| --- | --- | --- |
| ind | [Particle System Instance](part_system_create.md) | The particle system to change. |
| angle | [Real](../../../../GML_Overview/Data_Types.md) | The new angle of the particle system. |

 

#### Returns:

N/A

 

#### Example:

var \_mouse\_dir \= point\_direction(x, y, mouse\_x, mouse\_y);  

 part\_system\_angle(pt\_sys, \_mouse\_dir);

This gets the direction from the position of the instance towards the mouse cursor, and applies that as the angle of a particle system.
