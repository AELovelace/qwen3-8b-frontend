# particle\_get\_info

This function returns a [struct](../../../GML_Overview/Structs.md#struct) with information about a [Particle System Asset](../../../../The_Asset_Editors/Particle_Systems.md) created using [The Particle System Editor](../../../../The_Asset_Editors/Particle_Systems.md). It can also return information about a [Particle System Instance](Particle_Systems/part_system_create.md).

The returned struct is a [Particle System Info Struct](particle_get_info.md#particle_system_info_struct), which contains an [Array](../../../GML_Overview/Arrays.md) of [Particle Emitter Info Struct](particle_get_info.md#particle_emitter_info_struct)s. Each of these emitter structs stores info on the particle type that the emitter uses in its parttype variable, which contains a [Particle Type Info Struct](particle_get_info.md#particle_type_info_struct).

In a simplified way, the contents of the struct returned by this function look something like the following:

part\_sys\_info\_struct \=  

 {  

     emitters:  

     \[  

         {  

             parttype:  

             {  

                 // Particle type properties...  

             }  

             // All other particle emitter properties...  

         }  

         // More emitters...  

     ]  

     // All other particle system properties...  

 };

Note that the emitters key can hold a value of 0 if the particle system has no emitters.

Note that an Emitter Info Struct's parttype key can be undefined when the emitter doesn't have a valid particle type set.

The tables below list all variables that are available in each of these three structs.

[Particle System Info](#)

Particle System Info Struct

| Variable Name | Data Type | Description |
| --- | --- | --- |
| name | [String](../../../GML_Overview/Data_Types.md) | The name of the particle system asset, or an empty string "" for a [Particle System Instance](Particle_Systems/part_system_create.md) not created from a [Particle System Asset](../../../../The_Asset_Editors/Particle_Systems.md). |
| xorigin | [Real](../../../GML_Overview/Data_Types.md) | The X coordinate of the particle system asset's origin. This will be 0 when the function is called on an instance that wasn't created from an asset. |
| yorigin | [Real](../../../GML_Overview/Data_Types.md) | The Y coordinate of the particle system asset's origin. This will be 0 when the function is called on an instance that wasn't created from an asset. |
| xdraw | [Real](../../../GML_Overview/Data_Types.md) | The X coordinate of the draw position for a particle system instance (see [part\_system\_position](Particle_Systems/part_system_position.md)). This will be 0 when the function is called on an asset. |
| ydraw | [Real](../../../GML_Overview/Data_Types.md) | The Y coordinate of the draw position for a particle system instance (see [part\_system\_position](Particle_Systems/part_system_position.md)). This will be 0 when the function is called on an asset. |
| angle | [Real](../../../GML_Overview/Data_Types.md) | The angle of the particle system instance (see [part\_system\_angle](Particle_Systems/part_system_angle.md)). |
| color | [Colour](../Colour_And_Alpha/Colour_And_Alpha.md) | The blend colour of the particle system instance (see [part\_system\_colour](Particle_Systems/part_system_colour.md)). |
| global\_space | [Boolean](../../../GML_Overview/Data_Types.md) | Whether this particle system has global space particles enabled (see [part\_system\_global\_space](Particle_Systems/part_system_global_space.md)). |
| oldtonew | [Boolean](../../../GML_Overview/Data_Types.md) | Whether old particles should be drawn behind new ones (true) or not (false). |
| emitters | [Array](../../../GML_Overview/Arrays.md) of [Particle Emitter Info Struct](particle_get_info.md#particle_emitter_info_struct) | An array of emitter info structs, ordered the same as in [The Particle System Editor](../../../../The_Asset_Editors/Particle_Systems.md). |

[Particle Emitter Info](#)

Particle Emitter Info Struct

| Variable Name | Data Type | Description |
| --- | --- | --- |
| ind | [Particle Emitter](Particle_Emitters/part_emitter_create.md) | The particle emitter. |
| name | [String](../../../GML_Overview/Data_Types.md) | The name of the particle emitter. |
| mode | [Particle Emitter Mode Constant](particle_get_info.md#particle_emitter_mode_constant) | The mode in which to emit particles. Either ps\_mode\_stream or ps\_mode\_burst. Only applies to particle system *assets*. |
| enabled | [Boolean](../../../GML_Overview/Data_Types.md) | Whether the particle emitter is enabled. |
| number | [Real](../../../GML_Overview/Data_Types.md) | The number of particles to create every frame if mode is ps\_mode\_stream or to create only once if mode is ps\_mode\_burst. Density (percent coverage) when in relative mode. |
| relative | [Boolean](../../../GML_Overview/Data_Types.md) | Whether the emitter is in relative mode, in which the number of particles created by the emitter is relative to the area of its region (see [part\_emitter\_relative](Particle_Emitters/part_emitter_relative.md)). |
| xmin | [Real](../../../GML_Overview/Data_Types.md) | The X coordinate of the left side of the emitter's region. |
| xmax | [Real](../../../GML_Overview/Data_Types.md) | The X coordinate of the right side of the emitter's region. |
| ymin | [Real](../../../GML_Overview/Data_Types.md) | The Y coordinate of the top of the emitter's region. |
| ymax | [Real](../../../GML_Overview/Data_Types.md) | The Y coordinate of the bottom of the emitter's region. |
| distribution | [Particle Emitter Distribution Constant](Particle_Emitters/part_emitter_region.md) | The distribution style of the particles. One of the ps\_distr\_\* constants. |
| shape | [Particle Emitter Shape Constant](Particle_Emitters/part_emitter_region.md) | The shape of the emitter's region. One of the ps\_shape\_\* constants. |
| parttype | [Particle Type Info Struct](particle_get_info.md#particle_type_info_struct) | The particle type info struct containing information about the particle type streamed by this emitter (if mode is ps\_mode\_stream), or about the type this emitter will burst (mode is ps\_mode\_burst) if the information is returned for a particle system asset. Can be undefined if the particle type that the emitter uses is set to an invalid reference. |
| delay\_min | [Real](../../../GML_Overview/Data_Types.md) | The minimum delay between particle bursts in stream mode, expressed in delay\_unit. |
| delay\_max | [Real](../../../GML_Overview/Data_Types.md) | The maximum delay between particle bursts in stream mode, expressed in delay\_unit. |
| delay\_unit | [Time Source Unit Constant](../../Time_Sources/Time_Source_Units.md) | The unit in which delay\_min and delay\_max are expressed |
| interval\_min | [Real](../../../GML_Overview/Data_Types.md) | The minimum time between particle bursts in stream mode, expressed in interval\_unit. |
| interval\_max | [Real](../../../GML_Overview/Data_Types.md) | The maximum time between particle bursts in stream mode, expressed in interval\_unit. |
| interval\_unit | [Time Source Unit Constant](../../Time_Sources/Time_Source_Units.md) | The unit in which interval\_min and interval\_max are expressed. |

[Particle Type Info](#)

Particle Type Info Struct

| Variable Name | Data Type | Description |
| --- | --- | --- |
| General | | |
| ind | [Particle Type](Particle_Types/part_type_create.md) | The particle type. This can be used e.g. with the function [part\_particles\_create](Particle_Systems/part_particles_create.md). |
| Shape / Sprite | | |
| sprite | [Sprite Asset](../../../../The_Asset_Editors/Sprites.md) | The sprite that the particle type uses or an invalid sprite handle (\-1). |
| frame | [Real](../../../GML_Overview/Data_Types.md) | The sprite subimage in case a sprite is used. |
| animate | [Boolean](../../../GML_Overview/Data_Types.md) | If true then the sprite is animated, starting from the frame subimage. |
| stretch | [Boolean](../../../GML_Overview/Data_Types.md) | If true then the animation is stretched over the particle's lifetime. |
| random | [Boolean](../../../GML_Overview/Data_Types.md) | If true then a random subimage is used instead of frame. |
| shape | [Particle Shape Constant](Particle_Types/part_type_shape.md) | The particle shape. One of the pt\_shape\_\* constants. Used only if the particle type doesn't use a sprite. |
| Size | | |
| size\_xmin | [Real](../../../GML_Overview/Data_Types.md) | The minimum size a particle of this type can have on the X axis when it is created (the size is determined randomly for each particle and can vary from size\_xmin to size\_xmax). |
| size\_ymin | [Real](../../../GML_Overview/Data_Types.md) | The minimum size a particle of this type can have on the Y axis when it is created (the size is determined randomly for each particle and can vary from size\_ymin to size\_ymax). |
| size\_xmax | [Real](../../../GML_Overview/Data_Types.md) | The maximum size a particle of this type can have on the X axis when it is created (the size is determined randomly for each particle and can vary from size\_xmin to size\_xmax). |
| size\_ymax | [Real](../../../GML_Overview/Data_Types.md) | The maximum size a particle of this type can have on the Y axis when it is created (the size is determined randomly for each particle and can vary from size\_ymin to size\_ymax). |
| size\_xincr | [Real](../../../GML_Overview/Data_Types.md) | The value to increase/decrease the particle size on the X axis by each frame. |
| size\_yincr | [Real](../../../GML_Overview/Data_Types.md) | The value to increase/decrease the particle size on the Y axis by each frame. |
| size\_xwiggle | [Real](../../../GML_Overview/Data_Types.md) | Value randomly added or subtracted from the particle's X size each frame. |
| size\_ywiggle | [Real](../../../GML_Overview/Data_Types.md) | Value randomly added or subtracted from the particle's Y size each frame. |
| Scale | | |
| xscale | [Real](../../../GML_Overview/Data_Types.md) | The X scale of the particle image (sprite or shape). |
| yscale | [Real](../../../GML_Overview/Data_Types.md) | The Y scale of the particle image (sprite or shape). |
| Life | | |
| life\_min | [Real](../../../GML_Overview/Data_Types.md) | The minimum life of particles of this type (in number of frames). |
| life\_max | [Real](../../../GML_Overview/Data_Types.md) | The maximum life of particles of this type (in number of frames). |
| Secondary Particles | | |
| death\_type | [Particle Type](Particle_Types/part_type_create.md) | The type of particle spawned on death or \-1. |
| death\_number | [Real](../../../GML_Overview/Data_Types.md) | The number of particles spawned on death. |
| step\_type | [Particle Type](Particle_Types/part_type_create.md) | The type of particle spawned each step or \-1. |
| step\_number | [Real](../../../GML_Overview/Data_Types.md) | The number of particles spawned each step. |
| Speed | | |
| speed\_min | [Real](../../../GML_Overview/Data_Types.md) | The minimum speed (in pixels per frame) of the particle when it's created (this starting speed is determined randomly for each particle and ranges from speed\_min to speed\_max). |
| speed\_max | [Real](../../../GML_Overview/Data_Types.md) | The maximum speed (in pixels per frame) of the particle when it's created (this starting speed is determined randomly for each particle and ranges from speed\_min to speed\_max). |
| speed\_incr | [Real](../../../GML_Overview/Data_Types.md) | The value to increase/decrease the particle speed by each frame. |
| speed\_wiggle | [Real](../../../GML_Overview/Data_Types.md) | A value randomly added or subtracted from the particle speed each frame. |
| Direction | | |
| dir\_min | [Real](../../../GML_Overview/Data_Types.md) | The minimum direction (in degrees) for a particle when it's created (this starting direction is determined randomly for each particle and ranges from dir\_min to dir\_max). |
| dir\_max | [Real](../../../GML_Overview/Data_Types.md) | The maximum direction (in degrees) for a particle when it's created (this starting direction is determined randomly for each particle and ranges from dir\_min to dir\_max). |
| dir\_incr | [Real](../../../GML_Overview/Data_Types.md) | The value to increase/decrease the particle direction by each frame. |
| dir\_wiggle | [Real](../../../GML_Overview/Data_Types.md) | A value randomly added or subtracted from the particle direction each frame. |
| Gravity | | |
| grav\_amount | [Real](../../../GML_Overview/Data_Types.md) | The amount of gravity applied to the particle each frame (in pixels per frame). |
| grav\_dir | [Real](../../../GML_Overview/Data_Types.md) | The gravity direction. |
| Orientation | | |
| ang\_min | [Real](../../../GML_Overview/Data_Types.md) | The minimum starting angle (in degrees) of the particle sprite when created (this starting angle is determined randomly for each particle and ranges from ang\_min to ang\_max). |
| ang\_max | [Real](../../../GML_Overview/Data_Types.md) | The maximum starting angle (in degrees) of the particle sprite when created (this starting angle is determined randomly for each particle and ranges from ang\_min to ang\_max). |
| ang\_incr | [Real](../../../GML_Overview/Data_Types.md) | The value to increase/decrease the particle angle by each frame. |
| ang\_wiggle | [Real](../../../GML_Overview/Data_Types.md) | A value randomly added or subtracted from the particle angle each frame. |
| ang\_relative | [Boolean](../../../GML_Overview/Data_Types.md) | If true then the particle angle is relative to its direction. |
| Color \& Alpha | | |
| color\_mode | [Real](../../../GML_Overview/Data_Types.md) | The color mode of the particle type. Can be one of these values:   0: Uses only one colour (color1)  1: Interpolates between two colours over time (color1, color2)  2: Interpolates between three colours over time (color1\-3)  3: Uses RGB range values (color1\-6 represent the parameters in order)  4: Uses HSV range values (color1\-6 represent the parameters in order)  5: Mixes two colours (color1, color2) |
| color1 | [Colour](../Colour_And_Alpha/Colour_And_Alpha.md) | See color\_mode description above for value |
| color2 | [Colour](../Colour_And_Alpha/Colour_And_Alpha.md) | See color\_mode description above for value |
| color3 | [Colour](../Colour_And_Alpha/Colour_And_Alpha.md) | See color\_mode description above for value |
| color4 | [Colour](../Colour_And_Alpha/Colour_And_Alpha.md) | See color\_mode description above for value (only used for RGB, HSV modes) |
| color5 | [Colour](../Colour_And_Alpha/Colour_And_Alpha.md) | See color\_mode description above for value (only used for RGB, HSV modes) |
| color6 | [Colour](../Colour_And_Alpha/Colour_And_Alpha.md) | See color\_mode description above for value (only used for RGB, HSV modes) |
| alpha1 | [Real](../../../GML_Overview/Data_Types.md) | The alpha of the particle when created. |
| alpha2 | [Real](../../../GML_Overview/Data_Types.md) | The alpha of the particle when halfway through its lifespan. |
| alpha3 | [Real](../../../GML_Overview/Data_Types.md) | The alpha of the particle at the end of its lifespan. |
| additive | [Boolean](../../../GML_Overview/Data_Types.md) | If true then the particle is drawn with additive blending (i.e. using the [Blend Mode Constant](../GPU_Control/gpu_get_blendmode.md) bm\_add). |

 

Finally there is also a constant for the particle emitter mode:

Particle Emitter Mode Constant

| Constant | Description |
| --- | --- |
| ps\_mode\_stream | The particle emitter *streams* the given number of particles continuously (see [part\_emitter\_stream](Particle_Emitters/part_emitter_stream.md)) |
| ps\_mode\_burst | The particle emitter emits a single *burst* of the given number of particles (see [part\_emitter\_burst](Particle_Emitters/part_emitter_burst.md)) |

 

#### Syntax:

particle\_get\_info(partsys)

| Argument | Type | Description |
| --- | --- | --- |
| partsys | [Particle System Asset](../../../../The_Asset_Editors/Particle_Systems.md) or [Particle System Instance](Particle_Systems/part_system_create.md) | The particle system asset or instance to get the info from |

 

#### Returns:

[Particle System Info Struct](particle_get_info.md#particle_system_info_struct)

 

#### Example 1: Particle Type Info

var \_particle\_info \= particle\_get\_info(ps\_Clouds);  

 var \_asset\_name \= \_particle\_info.name;  

  

 var \_arr\_emitters \= \_particle\_info.emitters;  

 if (array\_length(\_arr\_emitters) \> 0\)  

 {  

     var \_type\_info \= \_arr\_emitters\[0].parttype;  

  

     if (\_type\_info.additive)  

     {  

         show\_debug\_message("The first emitter in {0} creates shiny particles!", \_asset\_name);  

     }  

 }
 

The above code first gets information from an existing [Particle System Asset](../../../../The_Asset_Editors/Particle_Systems.md) ps\_Clouds using particle\_get\_info and assigns the returned struct to a temporary variable \_particle\_info. It then looks up the emitters in the particle system through the [Particle System Info Struct](particle_get_info.md#particle_system_info_struct)'s emitters variable. If the particle system contains any emitters (i.e. the array's length is greater than 0\), the first emitter's parttype variable is assigned to a temporary variable \_type\_info and checked for additive blending (bm\_add). Finally a debug message is shown if additive blending is used for the particle type.

 

#### Example 2: Listing Emitter Names

var \_particle\_info \= particle\_get\_info(ps\_Environment);  

 var \_asset\_name \= \_particle\_info.name;  

  

 var \_emitter\_names \= array\_map(\_particle\_info.emitters, function(\_element, \_index) { return \_element.name; });  

 \_emitter\_names \= string\_join\_ext(", ", \_emitter\_names);  

  

 show\_debug\_message("{0} contains the following particle emitters: {1}", \_asset\_name, \_emitter\_names);
 

The above code first calls particle\_get\_info to retrieve information about an existing [Particle System Asset](../../../../The_Asset_Editors/Particle_Systems.md) ps\_Environment. The asset's name is stored in a temporary variable \_asset\_name. After that, an array of emitter names is generated from the [Particle System Info Struct](particle_get_info.md#particle_system_info_struct)'s emitters variable and converted to a string listing all names, separated by a comma, using [string\_join\_ext](../../Strings/string_join_ext.md). Finally a debug message displays the information in a readable form.
