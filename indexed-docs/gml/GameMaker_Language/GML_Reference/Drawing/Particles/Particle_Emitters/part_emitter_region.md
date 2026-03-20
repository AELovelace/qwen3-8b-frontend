# part\_emitter\_region

This function sets the region of a particle emitter within its particle system.

You specify the bounding box of the area within the system and then use any of a series of constants to define the final emitter shape within this bounding box as well as the distribution of particles within the shape. The available constants for distribution shapes are listed below:

| [Particle Emitter Shape Constant](part_emitter_region.md) | |
| --- | --- |
| Constant | Description |
| ps\_shape\_rectangle | A rectangular shape that fills the given area. |
| ps\_shape\_ellipse | An ellipse, with the width and height defined by the area. |
| ps\_shape\_diamond | A diamond shape with the points at half width and half height. |
| ps\_shape\_line | A single line, where the start point is the left and top and the end point is the right and bottom. |

 

Apart from the distribution shapes, you can also define the distribution curve for the particles that are to be emitted. The available constants for distribution curves are listed below:

| [Particle Emitter Distribution Constant](part_emitter_region.md) | |
| --- | --- |
| Constant | Description |
| ps\_distr\_linear | A linear distribution where all particles have an equal chance of appearing anywhere in the area. |
| ps\_distr\_gaussian | A gaussian distribution where more particles are generated in the center rather than the edges. |
| ps\_distr\_invgaussian | An inverse gaussian distribution where more particles are generated at the edges than center. |

 

  If you need the emitter to move with an instance, you will have to use this function in the Step event and update the emitter position that way. It is also worth noting that for point emissions where you do not need to create particles over an area or with a specific distribution, it is often easier to use [part\_particles\_create](../Particle_Systems/part_particles_create.md).

 

#### Syntax:

part\_emitter\_region(ps, ind, xmin, xmax, ymin, ymax, shape, distribution)

| Argument | Type | Description |
| --- | --- | --- |
| ps | [Particle System Instance](../Particle_Systems/part_system_create.md) | The particle system that the emitter is in. |
| ind | [Particle Emitter](part_emitter_create.md) | The index of the emitter to set. |
| xmin | [Real](../../../../GML_Overview/Data_Types.md) | The x coordinate of the left side of the region. |
| xmax | [Real](../../../../GML_Overview/Data_Types.md) | The x coordinate of the right side of the region. |
| ymin | [Real](../../../../GML_Overview/Data_Types.md) | The y coordinate of the top of the region. |
| ymax | [Real](../../../../GML_Overview/Data_Types.md) | The y coordinate of the bottom of the region. |
| shape | [Particle Emitter Shape Constant](part_emitter_region.md) | The shape of the region. |
| distribution | [Particle Emitter Distribution Constant](part_emitter_region.md) | The distribution style of the particles. |

 

#### Returns:

N/A

 

#### Example 1: Basic Use

Create Event

ps \= part\_system\_create();  

 pe \= part\_emitter\_create(ps);  

part\_emitter\_region(ps, pe, x \- 50, x \+ 50, y \- 50, y \+ 50, ps\_shape\_ellipse, ps\_distr\_linear);
 

The above code creates a new empty particle system instance and adds an emitter to it. It then sets the emitter's region to a 100px tall and 100px wide elliptical shape around the current (x, y) position of the instance running the code.

 

#### Example 2: Updating the Region of a Particle Emitter in the Step Event

Create Event

ps \= part\_system\_create();  

 pe \= part\_emitter\_create(ps);  

 pt \= part\_type\_create();  

 part\_emitter\_region(ps, pe, x \- 100, x \+ 100, y \- 100, y \+ 100, ps\_shape\_ellipse, ps\_distr\_gaussian);  

 part\_emitter\_stream(ps, pe, pt, 3\);

Step Event

part\_emitter\_region(ps, pe, x \- 100, x \+ 100, y \- 100, y \+ 100, ps\_shape\_ellipse, ps\_distr\_gaussian);

The code above shows how to update the region of a particle emitter every step.

In the Create event, a particle system is created and a particle emitter is added to it. A particle type is also created. The emitter's region is set a first time using part\_emitter\_region and it is set to stream three particles of the previously created type every step.

In the Step event, the emitter's region is set again using part\_emitter\_region.

 

#### Example 3: Retrieving an Emitter Defined in a Particle System Asset and Changing its Region

Create Event

ps \= part\_system\_create(ps\_snowflakes);  

 var \_info \= part\_system\_get\_info(ps);  

 var \_arr\_emitters \= \_info.emitters;  

 pe \= \-1;  

 for(var i \= 0;i \< array\_length(\_arr\_emitters);i\+\+)  

 {  

     if (\_arr\_emitters\[i].name \=\= "pe\_neon")  

     {  

         pe \= i;  

         break;  

     }  

 }  

 part\_emitter\_region(ps, pe, x \- 50, x \+ 50, y \- 50, y \+ 50, ps\_shape\_line, ps\_distr\_linear);

The code above shows how to change the region of a particle emitter in a particle system asset created in [The Particle System Editor](../../../../../The_Asset_Editors/Particle_Systems.md).

First, [part\_system\_create](../Particle_Systems/part_system_create.md) is called with ps\_snowflakes as the parameter, where ps\_snowflakes is a [Particle System Asset](../../../../../The_Asset_Editors/Particle_Systems.md) created in the Particle System Editor. Next, the information about this particle system is retrieved using [part\_system\_get\_info](../Particle_Systems/part_system_get_info.md). After this, a [for](../../../../GML_Overview/Language_Features/for.md) loop is used to find the index of the particle emitter named "pe\_neon" in the Particle System Editor (which must exist in ps\_snowflakes). Finally, the region of the particle emitter is set to be a 100px by 100px region around the calling instance using part\_emitter\_region.

Note that the emitter names that you set in the Particle System Editor cannot be used directly in GML, i.e. in the code above you cannot access the emitter properties using \_arr\_emitters\[pe\_neon] and so you need to lookup the emitter's index by name first.
