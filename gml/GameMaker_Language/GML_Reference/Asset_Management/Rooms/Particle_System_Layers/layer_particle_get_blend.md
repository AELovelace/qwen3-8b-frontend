# layer\_particle\_get\_blend

This function returns the blend colour of the given particle system element.

 

#### Syntax:

layer\_particle\_get\_blend(particle\_element\_id)

| Argument | Type | Description |
| --- | --- | --- |
| particle\_element\_id | [Particle System Element ID](layer_particle_get_id.md) | The unique ID value of the particle system element |

 

#### Returns:

[Colour](../../../Drawing/Colour_And_Alpha/Colour_And_Alpha.md)

 

#### Example:

var \_element\_id \= layer\_particle\_get\_id("Effects", "particle\_fireflies");  

 var \_colour \= layer\_particle\_get\_blend(\_element\_id);

The code above gets the element ID of a particle system element named "particle\_fireflies"  on a layer "Effects". It then retrieves the blend colour of the element and stores it in a variable for further use.
