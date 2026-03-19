# layer\_particle\_get\_xscale

This function returns the scale factor along the x axis applied to the given particle system element.

 

#### Syntax:

layer\_particle\_get\_xscale(particle\_element\_id)

| Argument | Type | Description |
| --- | --- | --- |
| particle\_element\_id | [Particle System Element ID](layer_particle_get_id.md) | The unique ID value of the particle system element |

 

#### Returns:

[Real](../../../../GML_Overview/Data_Types.md)

 

#### Example:

var \_element\_id \= layer\_particle\_get\_id("Particles", "particle\_smoke");  

 var \_xscale \= layer\_particle\_get\_xscale(\_element\_id);

The code above gets the element ID of a particle system element named "particle\_smoke"  on a layer "Particles". It then retrieves the scale factor along the x axis of the element and stores it in a variable for further use.
