# Particle System Elements

The GameMaker [Room Editor](../../../../../The_Asset_Editors/Rooms.md) allows you to add particle system assets that you create using [The Particle System Editor](../../../../../The_Asset_Editors/Particle_Systems.md) to [asset layers](../../../../../The_Asset_Editors/Room_Properties/Layer_Properties.md). A [Particle System Instance](../../../Drawing/Particles/Particle_Systems/part_system_create.md) is created at runtime for every particle system that you add to a layer in this way. You can also create particle systems on a layer in code using [part\_system\_create\_layer](../../../Drawing/Particles/Particle_Systems/part_system_create_layer.md). In both cases the newly created particle system is added as an element to the layer. Note that a particle system element corresponds to a [Particle System Instance](../../../Drawing/Particles/Particle_Systems/part_system_create.md).

To get or set any property of a particle system element on a layer, you first use [layer\_particle\_get\_id](layer_particle_get_id.md) to get the element ID and then use it in the other functions on this page to get or set the property you want:

var \_element\_id \= layer\_particle\_get\_id("Particles", "particle\_1");  

  

 layer\_particle\_x(\_element\_id, 100\);  

 layer\_particle\_blend(\_element\_id, c\_red);  

 var \_y \= layer\_particle\_get\_y(\_element\_id);  

 var \_alpha \= layer\_particle\_get\_alpha(\_element\_id);  

 // Etc.
 

## Function Reference

### General

- [layer\_particle\_get\_id](layer_particle_get_id.md)
- [layer\_particle\_get\_instance](layer_particle_get_instance.md)
- [layer\_particle\_get\_system](layer_particle_get_system.md)

### Positioning

- [layer\_particle\_x](layer_particle_x.md)
- [layer\_particle\_y](layer_particle_y.md)
- [layer\_particle\_angle](layer_particle_angle.md)
- [layer\_particle\_xscale](layer_particle_xscale.md)
- [layer\_particle\_yscale](layer_particle_yscale.md)
- [layer\_particle\_get\_x](layer_particle_get_x.md)
- [layer\_particle\_get\_y](layer_particle_get_y.md)
- [layer\_particle\_get\_angle](layer_particle_get_angle.md)
- [layer\_particle\_get\_xscale](layer_particle_get_xscale.md)
- [layer\_particle\_get\_yscale](layer_particle_get_yscale.md)

### Colour \& Alpha

- [layer\_particle\_blend](layer_particle_blend.md)
- [layer\_particle\_alpha](layer_particle_alpha.md)
- [layer\_particle\_get\_blend](layer_particle_get_blend.md)
- [layer\_particle\_get\_alpha](layer_particle_get_alpha.md)
