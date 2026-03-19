# layer\_particle\_get\_system

This function returns the particle system asset associated with the given particle system element.

 

#### Syntax:

layer\_particle\_get\_system(particle\_element\_id)

| Argument | Type | Description |
| --- | --- | --- |
| particle\_element\_id | [Particle System Element ID](layer_particle_get_id.md) | The unique ID value of the particle system element |

 

#### Returns:

[Particle System Asset](../../../../../The_Asset_Editors/Particle_Systems.md) or \-1 if the particle system element wasn't created from an asset

 

#### Example 1: Basic Use

var \_element\_id \= layer\_particle\_get\_id("Effects", "particle\_fire");  

 var \_ps\_asset \= layer\_particle\_get\_system(\_element\_id);

The code above first retrieves the ID of a particle element added to a layer "Effects" and named "particle\_fire". The particle system asset of this element is then retrieved with a call to layer\_particle\_get\_system and stored in a variable.

 

#### Example 2: Particle Systems Created in Code

var \_layer\_name \= "Effects";  

  

 ps\_empty \= part\_system\_create\_layer(\_layer\_name, false);  

 ps\_from\_asset \= part\_system\_create\_layer(\_layer\_name, false, ps\_portal);  

  

 var \_arr\_elements \= layer\_get\_all\_elements(\_layer\_name);  

 for(var i \= 0;i \< array\_length(\_arr\_elements);i\+\+)  

 {  

     var \_element\_id \= \_arr\_elements\[i];  

     var \_ps\_asset \= layer\_particle\_get\_system(\_element\_id);  

     show\_debug\_message("Particle System Asset for {0}: {1}", i, \_ps\_asset);  

 }
 

The code above first creates two new particle systems at run time on a layer "Effects" using the function [part\_system\_create\_layer](../../../Drawing/Particles/Particle_Systems/part_system_create_layer.md). After the two calls to the function the layer will have two elements on it. Next, all elements on the layer are retrieved using [layer\_get\_all\_elements](../General_Layer_Functions/layer_get_all_elements.md) and stored in a temporary variable. In a [for](../../../../GML_Overview/Language_Features/for.md) loop the array of elements is then traversed. For every element the ID is retrieved as well as the particle system asset the particle system was created from, and this information is shown in a debug message.

Note that the layer can only have particle system elements on it since  layer\_particle\_get\_system takes an element of type layerelementtype\_particlesystem.
