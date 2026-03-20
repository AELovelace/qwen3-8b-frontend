# layer\_particle\_get\_angle

This function gets the angle of the given particle system element.

  This function gets the angle of the *element*, which is different from the value set using [part\_system\_angle](../../../Drawing/Particles/Particle_Systems/part_system_angle.md).

 

#### Syntax:

layer\_particle\_get\_angle(particle\_element\_id)

| Argument | Type | Description |
| --- | --- | --- |
| particle\_element\_id | [Particle System Element ID](layer_particle_get_id.md) | The unique ID value of the particle system element |

 

#### Returns:

[Real](../../../../GML_Overview/Data_Types.md)

 

#### Example:

var \_element\_id \= layer\_particle\_get\_id("Particles", "particle\_smoke");  

 var \_angle \= layer\_particle\_get\_angle(\_element\_id);

The code above gets the element ID of a particle system element named "particle\_smoke"  on a layer "Particles". It then retrieves the angle of the element and stores it in a variable for further use.
