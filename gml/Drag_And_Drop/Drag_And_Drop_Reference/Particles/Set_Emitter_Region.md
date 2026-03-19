# title

This action is used to set the region and shape of an emitter within a particle system. You supply the particle system ID that the emitter belongs to (as returned by the action [Create Particle System](Create_Particle_System.md)) and then the actual emitter ID (as returned by the action [Create Particle Emitter](Create_Particle_Emitter.md)), and then give a shape for the emitter to take within the given bounding box values. The possible emitter shapes are:

To define your shapes, you give the coordinates for a "bounding box" into which the given shape will be placed (in the case of rectangle, ellipse and diamond shapes) or the first and second coordinates for the start and finish points (in the case of a line). All particles that are burst or streamed from the emitter will be created within the confines of the shape within this bounding box. You can also set the distribution of the particles with the option of:

- **Linear**: Particles will be created anywhere at random within the given shape.
- **Gaussian**: Particles will be created predominantly in the middle of the shape with fewer along the edges.
- **Inverse Gaussian**: Particles will be created predominantly along the edges of the shape with fewer in the middle.

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| System | The unique ID of the system the emitter belongs to |
| Emitter | The unique ID of the emitter to set the shape of |
| Shape | The particle shape that is to be used |
| Distribution | The distribution of particles within the given shape |
| Left | The position of the left side of the shape bounding box (in pixels) |
| Top | The position of the top of the shape bounding box (in pixels) |
| Right | The position of the right side of the shape bounding box (in pixels) |
| Bottom | The position of the bottom of the shape bounding box (in pixels) |

 

#### Example:

The above action block code will create a particle emitter, set its region, and then set it to emit a stream of particles.
