# particle\_exists

This function returns whether a [Particle System Asset](../../../../The_Asset_Editors/Particle_Systems.md) with the given index exists.

 

#### Syntax:

particle\_exists(index)

| Argument | Type | Description |
| --- | --- | --- |
| index | [Particle System Asset](../../../../The_Asset_Editors/Particle_Systems.md) | The index to check |

 

#### Returns:

[Boolean](../../../GML_Overview/Data_Types.md)

 

#### Example:

if (particle\_exists(ps\_fireworks))  

 {  

     part\_system\_create\_layer("Particles", false, ps\_fireworks);  

 }

The above code checks if a particle system asset ps\_fireworks exists. If it does, a new instance of it is created on a layer "Particles" using the function [part\_system\_create\_layer](Particle_Systems/part_system_create_layer.md).
