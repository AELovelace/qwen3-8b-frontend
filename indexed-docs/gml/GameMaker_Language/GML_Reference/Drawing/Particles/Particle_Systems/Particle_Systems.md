# Particle Systems

Before you can create particles you need to create a particle system. This is a "container" in which you create your particles and to which you add emitters (if you need them). You can put as many or as few particles into a system as you think necessary, and you can have as many systems as you think necessary too. However, it is always better to keep this number as small as possible since every system, emitter and particle takes up memory and having too many of them may slow your game down or cause problems. For example, if you need some effects to appear above instances, and other effects to appear below instances, you would create two systems and set their depths to get the desired effect, with all particles that are added to each system being drawn at the depth you specify.

Since a particle system is a dynamically created resource, you must create it and store the returned handle in a variable to reference the system in all further function calls, and it is very important that you also destroy the system when it is no longer needed or else you will have a memory leak that will slow down and eventually crash your game. It is also worth noting that particle systems will live on forever after they are created, even if the handle is no longer stored. So even if you change room or restart the game, the systems and the particles will remain, and be visible, in all further rooms so you better make sure you destroy them once you no longer need them.

 
## Creating a Particle System

To create an empty particle system instance in code you can use [part\_system\_create](part_system_create.md) or [part\_system\_create\_layer](part_system_create_layer.md):

ps \= part\_system\_create();

This creates a particle system instance with no particles or emitters in it.

  These functions return a particle system *instance*, which should not be confused with a particle system *asset* that you create in [The Particle System Editor](../../../../../The_Asset_Editors/Particle_Systems.md).

You then create particle types and add emitters to the particle system instance that spawn particles of the type:

pt \= part\_type\_create();  

 part\_type\_shape(pt, pt\_shape\_flare);  

  

 pe \= part\_emitter\_create(ps);  

 part\_emitter\_region(ps, pe, 0, 200, 0, 200, ps\_shape\_rectangle, ps\_distr\_linear);
 

To make the emitter continuously stream particles you can use [part\_emitter\_stream](../Particle_Emitters/part_emitter_stream.md):

part\_emitter\_stream(ps, pe, pt, 1\);

Defining a particle system instance entirely in code like this can be a lot of work, though there are ways to initialise it from an asset created in [The Particle System Editor](../../../../../The_Asset_Editors/Particle_Systems.md).

### Creating from a Particle System Asset

Instead of defining a particle system in code, you can pass a particle system asset to [part\_system\_create](part_system_create.md) / [part\_system\_create\_layer](part_system_create_layer.md):

ps \= part\_system\_create(ps\_my\_particle\_asset);

This creates a new particle system instance and initialises it according to how you set up the particle system asset in the Particle System Editor.

### Copy GML to Clipboard

Using [The Particle System Editor](../../../../../The_Asset_Editors/Particle_Systems.md)'s **Copy GML to Clipboard** button  you can generate the GML Code needed to create a particle system that's identical to the one you created. The code could, for example, go in an object's Create event: 

Create Event

var \_ps \= part\_system\_create();  

 part\_system\_draw\_order( \_ps, true);  

  

 var \_ptype1 \= part\_type\_create();  

 part\_type\_shape( \_ptype1, pt\_shape\_sphere );  

 part\_type\_size( \_ptype1, 1, 1, 0, 0 );  

 part\_type\_scale( \_ptype1, 1, 1\);  

 part\_type\_speed( \_ptype1, 2, 2, 0, 0\);  

 part\_type\_direction( \_ptype1, 0, 0, 4, 0\);  

 part\_type\_gravity( \_ptype1, 0, 270\);  

 part\_type\_orientation( \_ptype1, 0, 0, 0, 0, false);  

 part\_type\_colour3( \_ptype1, $7F7FFF, $FFFFFF, $FFEFBC );  

 part\_type\_alpha3( \_ptype1, 1, 1, 0\.169\);  

 part\_type\_blend( \_ptype1, true);  

 part\_type\_life( \_ptype1, 80, 80\);  

  

 var \_pemit1 \= part\_emitter\_create( \_ps );  

 part\_emitter\_region( \_ps, \_pemit1, \-64, 64, \-64, 64, ps\_shape\_rectangle, ps\_distr\_linear );  

 part\_emitter\_stream(\_ps, \_pemit1, \_ptype1, 1\);  

  

 part\_system\_position(\_ps, room\_width/2, room\_height/2\);
 

As the above code shows, emitters start streaming particles if you've configured them to be in **Stream** mode. By default, the particle system's position is set to the centre of the room.

  The particle system, emitters and types have to be destroyed manually (e.g. in the Clean Up event) to prevent memory leaks. Since emitters exist within systems, destroying a particle system destroys its emitters automatically.

## Accessing Particle Systems Added in the Room Editor

You can access particle systems added to a layer in [The Room Editor](../../../../../The_Asset_Editors/Rooms.md) using the name that you've given them:

At run time this name can be used to reference the [Particle System Instance](part_system_create.md) and you can use it in the part\_system\_\* functions to set, for example, the angle:

part\_system\_angle(particle\_trail, 30\);

Alternatively, you can change the particle system element instead through the [layer\_particle\_\*](../../../Asset_Management/Rooms/Particle_System_Layers/Particle_System_Elements.md) functions. For this you first get the element ID using [layer\_particle\_get\_id](../../../Asset_Management/Rooms/Particle_System_Layers/layer_particle_get_id.md), which you pass the layer and the name *as a string*.

var \_element\_id \= layer\_particle\_get\_id("Particles", "particle\_trail");  

 layer\_particle\_angle(\_element\_id, 30\);

Note that some properties of the element are identical to properties of the particle system (position, angle, colour and alpha). Changing these properties on the element does not change the properties of the particle system itself and vice versa.

## Function Reference

### Setting Up

- [part\_system\_exists](part_system_exists.md)
- [part\_system\_get\_info](part_system_get_info.md)
- [part\_system\_create](part_system_create.md)
- [part\_system\_create\_layer](part_system_create_layer.md)
- [part\_system\_get\_layer](part_system_get_layer.md)
- [part\_system\_layer](part_system_layer.md)
- [part\_system\_depth](part_system_depth.md)
- [part\_system\_position](part_system_position.md)
- [part\_system\_angle](part_system_angle.md)
- [part\_system\_global\_space](part_system_global_space.md)
- [part\_system\_colour](part_system_colour.md)
- [part\_system\_clear](part_system_clear.md)
- [part\_system\_destroy](part_system_destroy.md)
- [part\_particles\_clear](part_particles_clear.md)
- [part\_particles\_count](part_particles_count.md)

### Updating and Drawing

Once particles are added to a particle system and then burst or streamed into the room, they are normally automatically updated each step and drawn based on the parameters that you have used to define them. However it can sometimes be necessary to control when and how the system is updated as well as how the system should be drawn, and for that GameMaker provides the following functions:

- [part\_system\_automatic\_update](part_system_automatic_update.md)
- [part\_system\_automatic\_draw](part_system_automatic_draw.md)
- [part\_system\_update](part_system_update.md)
- [part\_system\_drawit](part_system_drawit.md)
- [part\_system\_draw\_order](part_system_draw_order.md)

### Creating Particles

You can use [particle emitters](../Particle_Emitters/Particle_Emitters.md) to burst or stream particles from an area, but in many cases these are not necessary and it is actually better to just create the particles directly using the following functions:

- [part\_particles\_create](part_particles_create.md)
- [part\_particles\_create\_colour](part_particles_create_colour.md)
- [part\_particles\_burst](part_particles_burst.md)
