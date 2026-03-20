# Particles

For complex things in GameMaker you would normally have an [object](../../../../The_Asset_Editors/Objects.md) and create [instances](../../Asset_Management/Instances/Instances.md) of that object around the room. However, for graphical effects, this can be expensive as every instance comes with a "cost" in processing due to the variables it contains and the code it has in the different events. You can reduce this cost by turning to [tilemap layers](../../../../The_Asset_Editors/Room_Properties/Layer_Properties.md) and [asset layers](../../../../The_Asset_Editors/Room_Properties/Layer_Properties.md) for drawing your graphics needs but those are generally static and cannot be changed or moved around much. However, there is one other option for drawing fast yet versatile graphics effects in your games, and that is to use *particles*.

**Particles** are graphic resources that have certain properties which are defined within a *particle system*. These properties cannot be manipulated directly for individual particles, but are changed through the code that is used to define the individual particle and the system that it belongs to. They are very useful for creating beautiful and flashy effects (or subtle and discreet ones!) like explosions, decals, rain, snow, star fields and debris in a game without the CPU overhead that using instances has.

Mini TOC (placeholder)

1. Heading

## Using Particles

### Basic Setup

The basic setup for a particle system in code follows three steps, with the third step being optional depending on how you wish to create your particle effects:

- **Create a particle system**: The particle system is like a container in which particles are created and exist throughout their lifetime. We use code to create particle *types* that define a series of visual aspects and behaviours for our particles, and then we create particles of those types in the "container", either directly or using an *emitter*.
- **Create particle types**: Particle types are the graphic effect itself. You can have many different types, each with their own range of colours, alphas, sizes and movements, but it's important to note that you *do not have control over individual particles*. You define a series of parameters and every particle will be created to have a random spread of behaviours chosen from them.
- **Create emitters**: Emitters are an option that can be used to burst or stream particles from within very clearly defined limits. They are optional because you can create particles from any instance using the [part\_particles\_create](Particle_Systems/part_particles_create.md) and [part\_particles\_create\_colour](Particle_Systems/part_particles_create_colour.md)
 functions but they are not always adequate for every situation.

### Built\-in Effects

The easiest way of creating particles in your game with GameMaker is to use the built\-in effects mechanism. These effects are created using an internal particle system which is basically a very fast method for drawing graphical effects only and as such you do not have to worry about all the details (like memory management) when using these functions. You simply specify the type of effect, the position where it must be created, the size you want it to be and finally, its colour then let GameMaker do all the work.

To create a built\-in effect you can use [effect\_create\_depth](effect_create_depth.md) or [effect\_create\_layer](effect_create_layer.md). To clear all particles created by these functions you can use [effect\_clear](effect_clear.md).

 
Even though these effects are limited in scope and customisation, they can still be used to create some simple, great effects with very little effort. For example, by creating a small puff of grey smoke below a moving missile in each step, a pretty convincing smoke trail is created, so even when you are an expert in particles it pays to remember that these effects exist as they can still save you some time.

However, the true potential of particles is in designing and creating your own effects using the powerful functions that the GameMaker Language supplies to you. You can find out more from each of the following sections:

- [Particle Systems](Particle_Systems/Particle_Systems.md)
- [Particle Types](Particle_Types/Particle_Types.md)
- [Particle Emitters](Particle_Emitters/Particle_Emitters.md)

  For a basic guide on how to design and create particles for your games (using GML Code or GML Visual) see [Guide To Using Particles](../../../../Additional_Information/Guide_To_Using_Particles.md).

## Usage Notes

Although particles are an excellent tool for creating effects, they do come with certain restrictions and good practices which need to be followed unless you want your game to suffer from poor performance or even potentially crash:

- Particle systems, particles and emitters take up memory and as such you should be very careful how you use them as it is very easy to cause a memory leak which will slow down and eventually crash your game. One way to cope with this is to have a *global* system with everything defined at the start of the game and removed at the end, but if you want a dynamic system then each particle and emitter (and the system itself) should be destroyed the moment it is no longer needed.
- Particles may be fast and light on the CPU, but they still require *some* processing and so you shouldn't have 40,000 of them bursting across the screen at a time. Limit them to those that are necessary to achieve a specific effect and no more.
- If you define your own particle sprite instead of using one of the 14 included sprites, you should try to keep it as small as possible to achieve the effect you require.
- Particles do *not* interact with anything. Should you need them to have any type of interaction with the user or any other instances in your game, you should be looking at using Instances instead as particles are purely graphic.
- Even though there is no technical limit to the number of systems, emitters and particles you can create in one game, you should try and limit everything to the minimum number possible to keep memory use as low as possible.
- On mobile devices, take care with particles as *drawing* them can be slow if they cover a large area of the screen (over\-draw on mobile devices is one of the main causes of slowdown).
- With HTML5 there is no additive blending, and unless you have WebGL enabled, you cannot have colour blending either.

## Function Reference

### Asset Info

  These functions retrieve information on [Particle System Asset](../../../../The_Asset_Editors/Particle_Systems.md)[s](Particle_Systems/Particle_Systems.md) created with [The Particle System Editor](../../../../The_Asset_Editors/Particle_Systems.md).

- [particle\_exists](particle_exists.md)
- [particle\_get\_info](particle_get_info.md)

### Creating Assets

- [particle\_add](particle_add.md)
- [particle\_delete](particle_delete.md)

### Simple Effects

- [effect\_create\_depth](effect_create_depth.md)
- [effect\_create\_layer](effect_create_layer.md)
- [effect\_create\_below](effect_create_below.md)
- [effect\_create\_above](effect_create_above.md)
- [effect\_clear](effect_clear.md)

### [Particle Systems](Particle_Systems/Particle_Systems.md)

### [Particle Types](Particle_Types/Particle_Types.md)

### [Particle Emitters](Particle_Emitters/Particle_Emitters.md)
