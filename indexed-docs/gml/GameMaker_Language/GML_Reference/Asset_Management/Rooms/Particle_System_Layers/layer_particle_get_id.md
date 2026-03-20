# layer\_particle\_get\_id

This function gets the unique ID value of the particle system element on the given layer by the name assigned to it in the Room Editor (as a string).

#### Syntax:

layer\_particle\_get\_id(layer\_id, particle\_element\_name)

| Argument | Type | Description |
| --- | --- | --- |
| layer\_id | [Layer](../General_Layer_Functions/layer_get_id.md) or [String](../../../../GML_Overview/Data_Types.md) | The handle or name of the layer |
| particle\_element\_name | [String](../../../../GML_Overview/Data_Types.md) | The name of the particle system element, as defined in the Room Editor |

 

#### Returns:

[Particle System Element ID](layer_particle_get_id.md)

 

#### Example:

var \_element\_id \= layer\_particle\_get\_id("Particles", "particle\_trail");  

 layer\_particle\_x(\_element\_id, 200\);  

 layer\_particle\_y(\_element\_id, 400\);

The code above first gets the element ID of a particle system element named "particle\_trail" that was added to a layer "Particles" in the Room Editor. It then changes the element's x to 200 and its y to 400\.
