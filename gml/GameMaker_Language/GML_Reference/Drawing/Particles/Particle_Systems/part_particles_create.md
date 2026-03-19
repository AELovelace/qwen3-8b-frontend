# part\_particles\_create

This function permits you to quickly and easily create particles at any position in a particle system.

It is ideal for those effects that do not require any of the functionality offered by [Particle Emitters](../Particle_Emitters/Particle_Emitters.md) (for example, to create smoke from a missile, or a simple explosion effect).

  You must have created the particle system and the particle type previously for this function to be used.

 

#### Syntax:

part\_particles\_create(ind, x, y, parttype, number)

| Argument | Type | Description |
| --- | --- | --- |
| ind | [Particle System Instance](part_system_create.md) | The particle system. |
| x | [Real](../../../../GML_Overview/Data_Types.md) | The x coordinate of where to create the particles. |
| y | [Real](../../../../GML_Overview/Data_Types.md) | The y coordinate of where to create the particles. |
| parttype | [Particle Type ID](../Particle_Types/part_type_create.md) | The index (type) of the particles to be created. |
| number | [Real](../../../../GML_Overview/Data_Types.md) | The number of particles to create. |

 

#### Returns:

N/A

 

#### Example:

if (mouse\_check\_button(mb\_left))  

 {  

     part\_particles\_create(sname, mouse\_x, mouse\_y, p\_CursorEffect, 5\);  

 }

The above code checks for the left mouse button being pressed and if it returns true it generates 5 particles at the mouse position.
