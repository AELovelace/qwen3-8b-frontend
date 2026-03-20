# layer\_particle\_get\_instance

This function returns a reference to the particle system instance associated with the given particle system element.

 

#### Syntax:

layer\_particle\_get\_instance(particle\_element\_id)

| Argument | Type | Description |
| --- | --- | --- |
| particle\_element\_id | [Particle System Element ID](layer_particle_get_id.md) | The unique ID value of the particle system element |

 

#### Returns:

[Particle System Instance](../../../Drawing/Particles/Particle_Systems/part_system_create.md)

 

#### Example:

var \_element\_id \= layer\_particle\_get\_id("Effects", "particle\_fireworks\_1");  

 var \_ps\_instance \= layer\_particle\_get\_instance(\_element\_id);  

 part\_system\_position(\_ps\_instance, x, y);  

 part\_system\_angle(\_ps\_instance, direction);

The code above first gets the ID of a particle system element added in the Room Editor to a layer "Effects" and named "particle\_fireworks\_1". It then passes the element ID to layer\_particle\_get\_instance to obtain the particle system instance corresponding to the element. Finally, the particle system instance's position and angle are set to the ([x](../../Instances/Instance_Variables/x.md), [y](../../Instances/Instance_Variables/y.md)) and [direction](../../Instances/Instance_Variables/direction.md) of the calling instance, respectively.

Note that this code modifies the particle system *instance's* position and angle rather than the particle system *element's* position and angle (which you would set with [layer\_particle\_x](layer_particle_x.md), [layer\_particle\_y](layer_particle_y.md) and [layer\_particle\_angle](layer_particle_angle.md) instead).
