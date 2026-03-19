# physics\_particle\_create

With this function you can create a single particle anywhere within your game room, setting certain flags and properties. The "flags" are the return value of a combination of the following **constants**:

| [Physics Particle Flag Constant](physics_particle_create.md) | |
| --- | --- |
| Constant | Description |
| phy\_particle\_flag\_water | The default properties for a soft body particle. |
| phy\_particle\_flag\_zombie | A zombie particle is one that will be destroyed after a single step with all others flagged in this way. |
| phy\_particle\_flag\_wall | This defines the particle as *static*, essentially creating it as an immovable object in the physics simulation, as they will remain in a fixed position no matter what collides with them. You should use this flag rather than set the density to 0\. |
| phy\_particle\_flag\_spring | Spring particles produce the effect of being attached to one another, as if by a spring. Particles created with this flag are "connected" in pairs, with each particle being connected to the one that was closest to it at the time of creation. Once paired, particles do not change "partners" , and the farther an external force pulls them from one another, the greater the power with which they will collide when that external force is removed. Note that no matter how far paired particles get from each another, the connection between them will not snap. |
| phy\_particle\_flag\_elastic | Elastic particles deform and may also bounce when they collide with other rigid bodies in the physics simulation. |
| phy\_particle\_flag\_viscous | A viscous particle is one that exhibits "clinginess" or "stickiness", like oil. Viscous particles will clump and stick together more. |
| phy\_particle\_flag\_powder | Powder particles produce a scattering effect such as you might see with sand or dust. |
| phy\_particle\_flag\_tensile | Tensile particles are used to produce the effect of surface tension, or the taut curvature on the surface of a body of liquid. They might be used, for example, to create the surface tension you would see on a drop of water. Once the tension is broken, the particles bounce as if they were elastic, but also continue to attract each other. As a result, particles tend to form clusters as they bounce. |
| phy\_particle\_flag\_colourmixing | Colour\-mixing particles take on some of the colour of other particles with which they collide. Note that if only one of the two colliding particles is a colour\-mixing one, the other particle retains its pre\-collision colour. |

These flags use bit\-masking to create a final output value that is then checked to set the different basic properties of the particle (with the base property always being that of phy\_particle\_flag\_water). For example, if you want to simulate a viscous liquid with surface tension you would use the [bitwise *or*](../../../../Additional_Information/Bitwise_Operators.md) "\|" to flag the appropriate bits as shown in the example below. In this way you can set different properties (other than the global properties) for each individual particle created.

Other than the flags, you can also set the position in the room to create the particle at, the initial horizontal and vertical velocity, the initial colour and alpha, as well as the user **category**. The colour and alpha values are only used when drawing the particle using the function [physics\_particle\_draw()](physics_particle_draw.md), but the category value is used in multiple other functions. This value is an arbitrary integer value that you give each particle that you want to have similar properties, and it can be used to set flags later for that specific category as well as a number of other things. For example, if you have defined a "water" and an "oil" particle, you would give all those particles flagged as "water" the user category of 1 and all those particles created as "oil" the user category of 2, permitting you to later target a single category to change its flags or get specific data.

  You can use any integer value for the category **except 0** which is reserved by the simulation and is used to select all categories in other functions (like for drawing).

The function returns a unique index (or ID) value for the particle which can be stored in a variable to be used in other functions that reference the particle directly.

 

#### Syntax:

physics\_particle\_create(flags, x, y, xv, yv, col, alpha, category)

| Argument | Type | Description |
| --- | --- | --- |
| flags | [Physics Particle Flag Constant](physics_particle_create.md)(s) | The flags to set on the particle. |
| x | [Real](../../../GML_Overview/Data_Types.md) | The x position to create the particle at. |
| y | [Real](../../../GML_Overview/Data_Types.md) | The y position to create the particle at. |
| xv | [Real](../../../GML_Overview/Data_Types.md) | The initial horizontal velocity. |
| yv | [Real](../../../GML_Overview/Data_Types.md) | The initial vertical velocity. |
| col | [Colour](../../Drawing/Colour_And_Alpha/Colour_And_Alpha.md) | The base colour to use for the particle. |
| alpha | [Real](../../../GML_Overview/Data_Types.md) | The base alpha to use for the particle. |
| category | [Real](../../../GML_Overview/Data_Types.md) | The user defined category to which the particle belongs. |

 

#### Returns:

[Physics Particle ID](physics_particle_create.md)

 

#### Example:

var flags \= phy\_particle\_flag\_water \| phy\_particle\_flag\_viscous \| phy\_particle\_flag\_tensile;  

 var x\_vel \= lengthdir\_x(5, image\_angle);  

 var y\_vel \= lengthdir\_y(5, image\_angle);  

 var p \= physics\_particle\_create(flags, x, y, x\_vel, y\_vel, c\_white, 1, 1\);

The above code will create variables to set the particle type and its initial velocity, then use these to create a particle at the instances x/y position.
