# physics\_particle\_group\_get\_data

This function returns various pieces of information about a group of particles in the physics simulation using the given flags checked. The group index (its ID) is that which was returned by the function [physics\_particle\_group\_end](physics_particle_group_end.md), and the buffer used must have been created previously using the function [buffer\_create](../../Buffers/buffer_create.md). It should be of the "grow" type, with the size being approximately that of the expected return data. The flags themselves are set using the constants given below, and you would use the [bitwise *or*](../../../../Additional_Information/Bitwise_Operators.md) \| to create a single flag value to get the desired information.

| Constant | Description | Data Type |
| --- | --- | --- |
| phy\_particle\_data\_flag\_typeflags | The flags value for the particle. | buffer\_u32 |
| phy\_particle\_data\_flag\_position | The x and y position of the particle. | 2 x buffer\_f32 |
| phy\_particle\_data\_flag\_velocity | The horizontal and vertical speed. | 2 x buffer\_f32 |
| phy\_particle\_data\_flag\_colour | The colour and alpha value (hexadecimal). | buffer\_f32 |
| phy\_particle\_data\_flag\_category | The particle category (as defined when you created the group to which it belongs). | buffer\_u32 |

 

#### Syntax:

physics\_particle\_group\_get\_data(group, buffer, flags)

| Argument | Type | Description |
| --- | --- | --- |
| group | [Physics Particle Group ID](../../../../../GameMaker_Language/GML_Reference/Physics/Soft_Body_Particles/physics_particle_group_end.md) | The group index (ID) of the particle group to get the data from. |
| buffer | [Buffer](../../../../../GameMaker_Language/GML_Reference/Buffers/buffer_create.md) | The (previously created) buffer to store the data. |
| flags | [Physics Particle Data Flag Constant](../../../../../GameMaker_Language/GML_Reference/Physics/Soft_Body_Particles/physics_particle_get_data.md)(s) | The flags to use to extract data about specific particle types. |

 

#### Returns:

N/A

 

#### Example:

var count \= physics\_particle\_group\_count(gp);  

 var flags \= phy\_particle\_data\_flag\_position \| phy\_particle\_data\_flag\_colour;  

 if (count \> 0\)  

 {  

     var buffer \= buffer\_create(count \* 12, buffer\_grow, 4\);  

     physics\_particle\_group\_get\_data(gp, buffer, flags);  

     for (var n \= 0; n \< count; n\+\+)  

     {  

         var xx \= buffer\_read(buffer, buffer\_f32\);  

         var yy \= buffer\_read(buffer, buffer\_f32\);  

         var argb \= buffer\_read(buffer, buffer\_u32\);  

         var alpha \= (argb \>\> 24\) \& 255;  

         draw\_sprite\_ext(sprBlob, 0, xx, yy, 1, 1, 0, c\_green, alpha);  

     }  

     buffer\_delete(buffer);  

 }

The above code gets the position and velocity of the every particle in the group indexed by the variable gp, stores the buffer data in a number of variables, and then uses that to draw a sprite at the position of each particle in the group.
