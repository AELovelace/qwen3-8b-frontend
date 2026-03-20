# physics\_particle\_get\_data\_particle

This function returns various pieces of information about a single particle in the physics simulation using the given flags checked.

The particle index (its ID) is that which was returned by the function [physics\_particle\_create](physics_particle_create.md), and the buffer used must have been created previously using the function [buffer\_create](../../Buffers/buffer_create.md). It should be of the "grow" type, with the size being approximately that of the expected return data. The flags themselves are set using the constants given below, and you would use the bitwise *or* "\|" to create a single flag value to get the desired information.

| Constant | Description | Data Type |
| --- | --- | --- |
| phy\_particle\_data\_flag\_typeflags | The flags value for the particle. | buffer\_u32 |
| phy\_particle\_data\_flag\_position | The x and y position of the particle. | 2 x buffer\_f32 |
| phy\_particle\_data\_flag\_velocity | The horizontal and vertical speed. | 2 x buffer\_f32 |
| phy\_particle\_data\_flag\_colour | The colour and alpha value (hexadecimal). | buffer\_u32 |
| phy\_particle\_data\_flag\_category | The particle category (as defined when you created the particle). | buffer\_u32 |

 

#### Syntax:

physics\_particle\_get\_data\_particle(ind, buffer, flags)

| Argument | Type | Description |
| --- | --- | --- |
| ind | [Physics Particle ID](physics_particle_create.md) | The index (ID) of the particle to get the data from. |
| buffer | [Buffer](../../Buffers/buffer_create.md) | The (previously created) buffer to store the data. |
| flags | [Physics Particle Data Flag Constant](physics_particle_get_data.md)(s) | The flags to use to extract data about specific particle types. |

 

#### Returns:

N/A

 

#### Example:

var part \= physics\_particle\_create(flags, x, y, x\_vel, y\_vel, c\_white, 1, 1\)  

 var flags \= phy\_particle\_data\_flag\_position \| phy\_particle\_data\_flag\_velocity;  

 var buffer \= buffer\_create(16, buffer\_grow, 4\);  

 physics\_particle\_get\_data\_particle(part, buffer, flags);  

 px \= buffer\_read(buffer, buffer\_f32\);  

 py \= buffer\_read(buffer, buffer\_f32\);  

 pvelx \= buffer\_read(buffer, buffer\_f32\);  

 pvely \= buffer\_read(buffer, buffer\_f32\);  

 buffer\_delete(buffer);

The above code gets the position and velocity of the particle indexed by the variable part and stores the data in a number of variables.
