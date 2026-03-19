# layer\_particle\_get\_alpha

This function returns the alpha value of the given particle system element.

 

#### Syntax:

layer\_particle\_get\_alpha(particle\_element\_id)

| Argument | Type | Description |
| --- | --- | --- |
| particle\_element\_id | [Particle System Element ID](layer_particle_get_id.md) | The unique ID value of the particle system element |

 

#### Returns:

[Real](../../../../GML_Overview/Data_Types.md)

 

#### Example:

var \_element\_id \= layer\_particle\_get\_id("Effects", "particle\_fireflies");  

 var \_alpha \= layer\_particle\_get\_alpha(\_element\_id);

The code above gets the element ID of a particle system element named "particle\_fireflies"  on a layer "Effects". It then retrieves the alpha value of the element and stores it in a variable for further use.
