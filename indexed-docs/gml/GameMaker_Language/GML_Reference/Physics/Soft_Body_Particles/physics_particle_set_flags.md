# physics\_particle\_set\_flags

With this function you can change the particle flags for an individual particle. The index value is the particle ID as returned by the function [physics\_particle\_create()](physics_particle_create.md), while the flags are the return value of a combination of the following **constants**:

| Constant | Description |
| --- | --- |
| phy\_particle\_flag\_water | The default properties for a soft body particle. |
| phy\_particle\_flag\_zombie | A zombie particle is one that will be destroyed in a single step with all others flagged in this way. |
| phy\_particle\_flag\_wall | This defines the particle as *static*, essentially creating it as an immovable object in the physics simulation, as they will remain in a fixed position no matter what collides with them. You should use this flag rather than set the density to 0\. |
| phy\_particle\_flag\_spring | Spring particles produce the effect of being attached to one another, as if by a spring. Particles created with this flag are "connected" in pairs, with each particle being connected to the one that was closest to it at the time of creation. Once paired, particles do not change "partners" , and the farther an external force pulls them from one another, the greater the power with which they will collide when that external force is removed. Note that no matter how far paired particles get from each another, the connection between them will not snap. |
| phy\_particle\_flag\_elastic | Elastic particles deform and may also bounce when they collide with other rigid bodies in the physics simulation. |
| phy\_particle\_flag\_viscous | A viscous particle is one that exhibits "clinginess" or "stickiness", like oil. Viscous particles will clump and stick together more. |
| phy\_particle\_flag\_powder | Powder particles produce a scattering effect such as you might see with sand or dust. |
| phy\_particle\_flag\_tensile | Tensile particles are used to produce the effect of surface tension, or the taut curvature on the surface of a body of liquid. They might be used, for example, to create the surface tension you would see on a drop of water. Once the tension is broken, the particles bounce as if they were elastic, but also continue to attract each other. As a result, particles tend to form clusters as they bounce. |
| phy\_particle\_flag\_colourmixing | Colour\-mixing particles take on some of the colour of other particles with which they collide. Note that if only one of the two colliding particles is a colour\-mixing one, the other particle retains its pre\-collision colour. |

These flags use bit\-masking to create a final output value that is then checked to set the different basic properties of the particle (with the base property always being that of phy\_particle\_flag\_water). For example, if you want to simulate a viscous liquid with surface tension you would use the [bitwise *or*](../../../../Additional_Information/Bitwise_Operators.md) "\|" to mask off the appropriate bits as shown in the example below. In this way you can set different properties (other than the global properties) for each individual particle created, should you wish.

 

#### Syntax:

physics\_particle\_set\_flags(index, flags)

| Argument | Type | Description |
| --- | --- | --- |
| index | Physics Particle ID | The index of the particle. |
| flags | Physics Particle Flag Constant(s) | The flags to set on the particle. |

 

#### Returns:

Real

 

#### Example:

var flags \= phy\_particle\_flag\_water \| phy\_particle\_flag\_viscous \| phy\_particle\_flag\_tensile;  

 physics\_particle\_set\_flags(p, flags);

The above code will create a variable to store the flags value and then use it to set the flags on a previously created particle with the index stored in the variable "p".
