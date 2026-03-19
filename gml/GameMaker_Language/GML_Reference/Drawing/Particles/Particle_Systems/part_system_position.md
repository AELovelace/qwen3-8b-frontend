# part\_system\_position

This function sets the base position for the given particle system instance. As a result, all particles created in this system will now be drawn relative to the new position.

Note that the position set using this function is relative to the particle system instance's corresponding layer element, if any:

- For particle system instances created using [part\_system\_create](part_system_create.md) this position will be relative to the room's (0, 0\) position.
- For particle system instances created using [part\_system\_create\_layer](part_system_create_layer.md) or added to an asset layer in [The Room Editor](../../../../../The_Asset_Editors/Rooms.md) this position will be relative to the corresponding layer element.

  This function will change **everything** within the particle system, so if you have an emitter at position (100, 100\) and then set the particle system position to (0, 100\), the emitter will now draw at (100, 200\). The same goes if you shift the system and then create the emitter, as even though you create it at (100, 100\) it will be drawn at (100, 200\).

 

#### Syntax:

part\_system\_position(ind, x, y)

| Argument | Type | Description |
| --- | --- | --- |
| ind | [Particle System Instance](part_system_create.md) | The particle system to change |
| x | [Real](../../../../GML_Overview/Data_Types.md) | The new x coordinate of the particle system |
| y | [Real](../../../../GML_Overview/Data_Types.md) | The new y coordinate of the particle system |

 

#### Returns:

N/A

 

#### Example:

if (mouse\_check\_button\_pressed(mb\_left))  

 {  

     part\_system\_position(global.Sname, mouse\_x, mouse\_y);  

 }

The above code will check for the press of the mouse button and if it detects one, the particle system indexed in the global variable Sname is shifted to the mouse x/y position.
