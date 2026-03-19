# The Keyframe Data Struct

When you define a [keyframe struct](The_Keyframe_Struct.md) for a track, you need to also define the data that will be associated with it. This is comprised of different *channels*, where each channel is simply a Keyframe Data Struct. A channel can be given specific type of data depending on what type of track you are setting the keyframe data for.

A Keyframe Data Struct contains the following variables:

| [Sequence Keyframe Data Struct](The_Keyframe_Data_Struct.md) | | |
| --- | --- | --- |
| Variable | Type | Description |
| channel | [Real](../../../../GML_Overview/Data_Types.md) | This is the channel that the keyframe data should be applied to. It is a positive integer value starting at 0, and it's worth noting that when creating parameter tracks for "position" or "scale" keyframes, then you need to use very specific channel values. These are: channel 0 is the X position or the X scale, channel 1 is the Y position or Y scale. |
| spriteIndex | [Sprite Asset](../../../../../The_Asset_Editors/Sprites.md) | The sprite asset to use for the track. This property is only available for tracks of the type seqtracktype\_graphic and you can get or set it. |
| soundIndex | [Sound Asset](../../../../../The_Asset_Editors/Sounds.md) | The audio asset to use for the track. This property is only available for tracks of the type seqtracktype\_audio and you can get or set it. |
| particleSystemIndex | [Particle System Asset](../../../../../The_Asset_Editors/Particle_Systems.md) | The particle system asset used for the track. This property is only available for tracks of the type seqtracktype\_particlesystem and you can get or set it. |
| playbackMode | [Sequence Audio Key Constant](The_Keyframe_Data_Struct.md) | The playback mode for the sound. This property is only available for tracks of the type seqtracktype\_audio and you can get or set it. The property should be one of the constants given in the table below this one. |
| curve | [Animation Curve Struct](../../Animation_Curves/animcurve_get.md) | This property requires an animation curve struct (see [here](../../Animation_Curves/animcurve_channel_new.md) for more information) and is only available for tracks of the type seqtracktype\_real. If no curve struct is used then the value for this property will be \-1\. |
| value | [Real](../../../../GML_Overview/Data_Types.md) | This property is simply a value that is associated with the keyframe data channel, and is only available for tracks of the type seqtracktype\_real when no curve struct is supplied. This can be, for example, the X or Y position of the track if placed inside a **"position"** parameter track. |
| colour | [Array](../../../../GML_Overview/Arrays.md) of [Real](../../../../GML_Overview/Data_Types.md)s | This property returns (or requires, if being set) an [array](../../../../GML_Overview/Arrays.md) for the colour value of the keyframe with the format \[A, R, G, B]. This is only available for tracks of the type seqtracktype\_colour. Note that the values for each component should be expressed as between 0 and 1, where 0 corresponds to the HEX value \#00 and 1 corresponds to the HEX value \#FF (0 \- 255 as shown in the colour picker for colour tracks in the Sequence Editor). |
| sequence | [Sequence Object Struct](The_Sequence_Object_Struct.md) | This property will return (or requires, if being set) a [sequence object struct](The_Sequence_Object_Struct.md) and is only available for tracks of the type seqtracktype\_sequence. |
| objectIndex | [Object Asset](../../../../../The_Asset_Editors/Objects.md) | This property will return (or requires, if being set) an object asset and is only available for tracks of the type seqtracktype\_instance. |
| events | [Array](../../../../GML_Overview/Arrays.md) of [String](../../../../GML_Overview/Data_Types.md)s | This property allows access to the **events** and **broadcast messages** associated with the keyframe data struct. You can get or set this property, and when getting it an array of strings is returned, and when setting it an array of strings should be specified. For more information on events, please see the section [Sequence Events And Moments](../Sequence_Events_Moments_Broadcast.md). This property is only available for tracks of the type seqtracktype\_message. |
| event | [Method](../../../../GML_Overview/Method_Variables.md) | This property will return (or can be set to) the [method](../../../../GML_Overview/Method_Variables.md) associated with the keyframe data struct. If no method has been specified or you wish to remove the method, then the property should be \-1\. This property is only available for tracks of the type seqtracktype\_moment. |
| *Any additional variables listed in the table(s) below* | | |

 
 

The playbackMode variable can be one of the following constants:

| [Sequence Audio Key Constant](The_Keyframe_Data_Struct.md) | | |
| --- | --- | --- |
| Constant | Description | Value |
| seqaudiokey\_loop | The sound will loop when played. | 0 |
| seqaudiokey\_oneshot | The sound will only play once then stop. | 1 |

 

## Text Track Data

The struct will contain the following additional variables if assigned to a [text track](../../../../../The_Asset_Editors/Sequence_Properties/Text_in_Sequences.md) (seqtracktype\_text):

| [Sequence Keyframe Data Struct](The_Keyframe_Data_Struct.md) | | |
| --- | --- | --- |
| Variable | Type | Description |
| text | [String](../../../../GML_Overview/Data_Types.md) | This is the text string that is drawn on the track. |
| wrap | [Boolean](../../../../GML_Overview/Data_Types.md) | This is a boolean that indicates whether the text should be wrapped (true) or not (false). |
| alignmentH | [Text Horizontal Alignment Constant](../../Rooms/Text_Functions/layer_text_halign.md) | This is the horizontal alignment of the text, and will be one of the constants given below. |
| alignmentV | [Text Vertical Alignment Constant](../../Rooms/Text_Functions/layer_text_valign.md) | This is the vertical alignment of the text, and will be one of the constants given below. |
| fontIndex | [Font Asset](../../../../../The_Asset_Editors/Fonts.md) | This is the [Font Asset](../../../../../The_Asset_Editors/Fonts.md) used by the text track. |

 

alignmentH can be any of the following constants:

 
 

alignmentV can be any of the following constants:

 
  The constants seqtextkey\_left, seqtextkey\_center, seqtextkey\_right, seqtextkey\_justify, seqtextkey\_top, seqtextkey\_middle, seqtextkey\_bottom also work as alternatives for the constants listed above, however they are deprecated and only supported for legacy purposes.
