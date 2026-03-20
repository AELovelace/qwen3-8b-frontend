# physics\_particle\_delete

With this function you can delete (remove) a particle from the physics simulation in the current room. The function takes the unique ID of the particle to delete, as returned by the function [physics\_particle\_create()](physics_particle_create.md).

 

#### Syntax:

physics\_particle\_delete(ind)

| Argument | Type | Description |
| --- | --- | --- |
| ind | Physics Particle ID | The index (ID) of the particle to delete. |

 

#### Returns:

N/A

 

#### Example:

physics\_particle\_delete(part);

The above code will delete the particle with the ID stored in the variable "part" from the simulation.
