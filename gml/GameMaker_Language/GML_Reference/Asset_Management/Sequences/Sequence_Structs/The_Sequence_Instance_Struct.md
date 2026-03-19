# The Sequence Instance Struct

A sequence, when placed in a room, is placed as an **element** on the layer, and this element contains a **sequence instance**.  

This sequence instance will have the following properties in its [struct](../../../../GML_Overview/Structs.md):

| [Sequence Instance Struct](The_Sequence_Instance_Struct.md) | | |
| --- | --- | --- |
| Variable | Type | Description |
| sequence | [Sequence Object Struct](The_Sequence_Object_Struct.md) | This is the ID of the **sequence object** struct that the sequence instance has been created from (see [The Sequence Object Struct](The_Sequence_Object_Struct.md)). You can get or set this struct, and so change the base sequence that the instance is referencing. |
| headPosition | [Real](../../../../GML_Overview/Data_Types.md) | This is the current [playhead](#) position (in frames) for the sequence instance. You can get or set this value, but note that setting it to a value greater or less than the currently defined play region will have different effects depending on the type of playback set for the sequence. See [layer\_sequence\_headpos](../../Rooms/Sequence_Layers/layer_sequence_headpos.md) for more information. |
| headDirection | [Sequence Direction Constant](The_Sequence_Instance_Struct.md) | This is the current playback direction for the sequence instance. You can get or set this value using the constants given in the next table (Note that you can use the layer functions [layer\_sequence\_get\_headdir](../../Rooms/Sequence_Layers/layer_sequence_get_headdir.md) and [layer\_sequence\_headdir](../../Rooms/Sequence_Layers/layer_sequence_headdir.md) to get or set this value without having to access the struct directly). |
| speedScale | [Real](../../../../GML_Overview/Data_Types.md) | This property can be used to get or set the playback speed scale. The speed scale is a *multiplier*, where 1 is the default playback speed and values less than 1 will slow the playback and values larger than 1 will speed it up, e.g.: a value of 0\.5 would be half playback speed, while a value of 2 would be double playback speed. Note that you can use the layer functions [layer\_sequence\_get\_speedscale](../../Rooms/Sequence_Layers/layer_sequence_get_speedscale.md) and [layer\_sequence\_speedscale](../../Rooms/Sequence_Layers/layer_sequence_speedscale.md) to get or set this value without having to access the struct directly. |
| paused | [Boolean](../../../../GML_Overview/Data_Types.md) | You can check this property to see if a sequence has been paused or not, and it will be true if it has, or false otherwise. This is a **read\-only** property, but you can use the layer function [layer\_sequence\_pause](../../Rooms/Sequence_Layers/layer_sequence_pause.md) to pause playback, and [layer\_sequence\_play](../../Rooms/Sequence_Layers/layer_sequence_play.md) to resume it again if required. You can also check this property using the layer function [layer\_sequence\_is\_paused](../../Rooms/Sequence_Layers/layer_sequence_is_paused.md) rather than check the property in the struct directly. |
| finished | [Boolean](../../../../GML_Overview/Data_Types.md) | You can check this property to see if a sequence has finished playing or not, returning true if it is finished playing, and false otherwise. This property will only ever return true for tracks that are not set to loop or ping\-pong. You can also check this property using the layer function [layer\_sequence\_is\_finished](../../Rooms/Sequence_Layers/layer_sequence_is_finished.md) rather than check the property in the struct directly. |
| elementID | [Sequence Element ID](../../Rooms/Sequence_Layers/layer_sequence_create.md) | This property holds the ID of the sequence *element*. This ID is a simple identifying value that is associated with a layer in the Room Editor, and it can then be used with the appropriate [layer functions](../../Rooms/General_Layer_Functions/General_Layer_Functions.md) to find the layer the sequence has been assigned to or to change certain sequence properties without having to deal with the struct. |
| activeTracks | [Array](../../../../GML_Overview/Arrays.md) of [Sequence Active Track Struct](The_Sequence_Instance_Struct.md#activeTracks)s | This property will hold an array of "evaluation" structs containing information on the current state of each **asset track** in the sequence (graphics, sequence, audio, etc.). These are the top\-level tracks. For the contents of the asset track struct returned in each array entry, please see the section below. |

 
 

| [Sequence Direction Constant](The_Sequence_Instance_Struct.md) | | |
| --- | --- | --- |
| Constant | Description | Value |
| seqdir\_right | The sequence will play frames in an incremental order from left to right | 1 |
| seqdir\_left | The sequence will play frames in a decremental order from right to left | \-1 |

 

## activeTracks Struct

  Although this property already exists in the sequence instance struct in the Sequence Create event, it is only filled with tracks after the first Sequence Begin Step event. So the first time you will find values in this struct is during the first iteration of the Sequence Step Event.

The following table contains the properties that may be available to you when accessing an active track struct (as included in the activeTracks array of a Sequence Instance struct, explained above). Each asset track struct can have any of the properties listed in the table below, depending on the type of asset the track uses. *All values returned are for the current playhead position*.

  You can modify all these properties, except where specified as **read\-only.**

| [Sequence Active Track Struct](The_Sequence_Instance_Struct.md#activeTracks) | | |
| --- | --- | --- |
| Variable | Type | Description |
| Common | | |
| posx | [Real](../../../../GML_Overview/Data_Types.md) | The position of the asset in the sequence along the X axis for the track (all asset track types). |
| posy | [Real](../../../../GML_Overview/Data_Types.md) | The position of the asset in the sequence along the Y axis for the track (all asset track types). |
| rotation | [Real](../../../../GML_Overview/Data_Types.md) | The rotation of the asset in the sequence (all asset track types). |
| xorigin | [Real](../../../../GML_Overview/Data_Types.md) | The X origin of the asset for the track (group, particle system, instance, sequence, text and sprite asset track types). |
| yorigin | [Real](../../../../GML_Overview/Data_Types.md) | The Y origin of the asset for the track (group, particle system, instance, sequence, text and sprite asset track types). |
| matrix | [Matrix](../../../Maths_And_Numbers/Matrix_Functions/Matrix_Functions.md) | The transformation matrix of the track within the parent track's frame of reference (all asset track types). |
| parent | [Sequence Instance Struct](The_Sequence_Instance_Struct.md) | The parent sequence instance ID for the track. |
| track | [Sequence Track Struct](The_Track_Struct.md) | The [Track Struct](The_Track_Struct.md) that this track is based on. |
| activeTracks | [Array](../../../../GML_Overview/Arrays.md) of [Sequence Track Struct](The_Track_Struct.md)s | This is an array of evaluation structs for each parameter track that the asset track contains. The contents of each struct in the array are listed in the parameter [Track Struct](The_Track_Struct.md) section. |
| scalex | [Real](../../../../GML_Overview/Data_Types.md) | The scale of the asset in the sequence along the X axis for the track (group, particle system, instance, sequence, text and sprite asset track types). |
| scaley | [Real](../../../../GML_Overview/Data_Types.md) | The scale of the asset in the sequence along the Y axis for the track (group, particle system, instance, sequence, text and sprite asset track types). |
| colouradd  coloradd | [Array](../../../../GML_Overview/Arrays.md) | The colour add value. This is an array of 4 values each from 0 to 1 corresponding to [ARGB](#) values. These values are added to the colourmultiply values before the result is multiplied by the sequence element's colour and alpha value. |
| colourmultiply  colormultiply | [Array](../../../../GML_Overview/Arrays.md) | The colour multiply value for the asset on the track in the sequence at the current playhead position (sprite, instance and sequence tracks). This value will be an [array](../../../../GML_Overview/Arrays.md) of four ARGB values with the format \[A, R, G, B]. Note that the values for each component are expressed as between 0 and 1, where 0 corresponds to the HEX value \#00 and 1 corresponds to the HEX value \#FF (0 \- 255 as shown in the colour picker for colour multiply tracks in [The Sequence Editor](../../../../../The_Asset_Editors/Sequences.md)) (particle system, instance, text and sprite asset track types). |
| Instance and Sprite Asset Tracks | | |
| spriteIndex | [Sprite Asset](../../../../../The_Asset_Editors/Sprites.md) | The sprite assigned to this track. |
| imageindex | [Real](../../../../GML_Overview/Data_Types.md) | The image index for the asset on the track in the sequence. |
| imagespeed | [Real](../../../../GML_Overview/Data_Types.md) | The image speed for the asset on the track in the sequence. |
| Instance Asset Tracks | | |
| instanceID | [Object Instance](../../Instances/Instance_Variables/id.md) | The ID of the instance on this track. |
| Particle System Asset Tracks | | |
| particleSystemID | [Particle System Instance](../../../Drawing/Particles/Particle_Systems/part_system_create.md) | The ID of the particle system instance on this track. |
| Sequence Asset Tracks | | |
| sequenceID | [Sequence Asset](../../../../../The_Asset_Editors/Sequences.md) | The index of the sequence asset used by this track. |
| sequence | [Sequence Object Struct](The_Sequence_Object_Struct.md) | The sequence object struct. |
| Text Asset Tracks | | |
| frameSizeX | [Real](../../../../GML_Overview/Data_Types.md) | The horizontal size of the text frame. |
| frameSizeY | [Real](../../../../GML_Overview/Data_Types.md) | The vertical size of the text frame. |
| characterSpacing | [Real](../../../../GML_Overview/Data_Types.md) | The character spacing value. |
| lineSpacing | [Real](../../../../GML_Overview/Data_Types.md) | The line spacing value. |
| paragraphSpacing | [Real](../../../../GML_Overview/Data_Types.md) | The paragraph spacing value. |
| effectsEnabled | [Boolean](../../../../GML_Overview/Data_Types.md) | Whether [SDF Effects](../../../../../The_Asset_Editors/Sequence_Properties/Text_in_Sequences.md#sdf_effects) are enabled on this track. |
| glowEnabled | [Boolean](../../../../GML_Overview/Data_Types.md) | Whether the glow effect is enabled. |
| outlineEnabled | [Boolean](../../../../GML_Overview/Data_Types.md) | Whether the outline effect is enabled. |
| dropShadowEnabled | [Boolean](../../../../GML_Overview/Data_Types.md) | Whether the drop shadow effect is enabled. |
| thickness | [Real](../../../../GML_Overview/Data_Types.md) | The thickness of the SDF effect. See [SDF Effects](../../../../../The_Asset_Editors/Sequence_Properties/Text_in_Sequences.md#sdf_effects). |
| coreColour  coreColor | [Array](../../../../GML_Overview/Arrays.md) | An array of 4 values, each from 0 to 1, corresponding to [ARGB](#) values of the 'core' part of the glyph. See [SDF Effects](../../../../../The_Asset_Editors/Sequence_Properties/Text_in_Sequences.md#sdf_effects). |
| glowColour  glowColor | [Array](../../../../GML_Overview/Arrays.md) | An array of 4 values, each from 0 to 1, corresponding to [ARGB](#) values of the glow colour. See [SDF Effects](../../../../../The_Asset_Editors/Sequence_Properties/Text_in_Sequences.md#sdf_effects). |
| glowStart | [Real](../../../../GML_Overview/Data_Types.md) | The distance in pixels at which the glow effect starts. See [SDF Effects](../../../../../The_Asset_Editors/Sequence_Properties/Text_in_Sequences.md#sdf_effects). |
| glowEnd | [Real](../../../../GML_Overview/Data_Types.md) | The distance in pixels at which the glow effect ends. See [SDF Effects](../../../../../The_Asset_Editors/Sequence_Properties/Text_in_Sequences.md#sdf_effects). |
| outlineColour  outlineColor | [Array](../../../../GML_Overview/Arrays.md) | An array of 4 values, each from 0 to 1, corresponding to [ARGB](#) values of the outline colour. See [SDF Effects](../../../../../The_Asset_Editors/Sequence_Properties/Text_in_Sequences.md#sdf_effects). |
| outlineDist | [Real](../../../../GML_Overview/Data_Types.md) | The distance of the outline. See [SDF Effects](../../../../../The_Asset_Editors/Sequence_Properties/Text_in_Sequences.md#sdf_effects). |
| shadowColour  shadowColor | [Array](../../../../GML_Overview/Arrays.md) | An array of 4 values, each from 0 to 1, holding the ARGB components of the drop shadow. See [SDF Effects](../../../../../The_Asset_Editors/Sequence_Properties/Text_in_Sequences.md#sdf_effects). |
| shadowSoftness | [Real](../../../../GML_Overview/Data_Types.md) | The width of the drop shadow penumbra. See [SDF Effects](../../../../../The_Asset_Editors/Sequence_Properties/Text_in_Sequences.md#sdf_effects). |
| shadowOffsetX | [Real](../../../../GML_Overview/Data_Types.md) | The offset in pixels on the x axis of the drop shadow. See [SDF Effects](../../../../../The_Asset_Editors/Sequence_Properties/Text_in_Sequences.md#sdf_effects). |
| shadowOffsetY | [Real](../../../../GML_Overview/Data_Types.md) | The offset in pixels on the y axis of the drop shadow. See [SDF Effects](../../../../../The_Asset_Editors/Sequence_Properties/Text_in_Sequences.md#sdf_effects). |
| Sound Asset Tracks | | |
| soundIndex | [Sound Instance ID](../../Audio/audio_play_sound.md) | The ID of the sound instance that's playing on this track's emitter. |
| emitterIndex | [Audio Emitter ID](../../Audio/Audio_Emitters/audio_emitter_create.md) | The index of the audio emitter used by this track. |
| gain | [Real](../../../../GML_Overview/Data_Types.md) | The gain of the track, which is the emitter gain. |
| pitch | [Real](../../../../GML_Overview/Data_Types.md) | The pitch of the track, which is the emitter pitch. |
| falloff | [Real](../../../../GML_Overview/Data_Types.md) | The audio emitter's falloff value. |
| falloffRef | [Real](../../../../GML_Overview/Data_Types.md) | The audio emitter's falloff reference distance. |
| falloffMax | [Real](../../../../GML_Overview/Data_Types.md) | The audio emitter's falloff maximum distance. |
| falloffFactor | [Real](../../../../GML_Overview/Data_Types.md) | The audio emitter's falloff factor. |
