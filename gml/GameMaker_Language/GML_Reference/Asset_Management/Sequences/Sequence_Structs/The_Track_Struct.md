# The Track Struct

The track struct can be used either for top\-level [asset track](#)s or for sub\-track [parameter tracks](#), and the behaviour of the track is defined by two things, its **name** and its **type**. Track [structs](../../../../GML_Overview/Structs.md) are created using the function [sequence\_track\_new](../sequence_track_new.md) and can be retrieved from sequence assets using the activeTracks property of [The Sequence Instance Struct](The_Sequence_Instance_Struct.md) or the tracks property of [The Sequence Object Struct](The_Sequence_Object_Struct.md).

The properties available in the track struct are:

| [Sequence Track Struct](The_Track_Struct.md) | | |
| --- | --- | --- |
| Variable | Type | Description |
| type | [Sequence Track Type Constant](The_Track_Struct.md#type) | This contains a [Sequence Track Type Constant](The_Track_Struct.md#type) that describes the type of track. This can be any one of the constants given under the [Type](The_Track_Struct.md#type) section. |
| name | [String](../../../../GML_Overview/Data_Types.md) | When creating a "top\-level" asset track, the name you give here can be any string that you require to identify the track. However, for parameter tracks, you need to specify specific strings to tell GameMaker what kind of parameter track you are creating. This is expanded upon under the [Name](The_Track_Struct.md#name) section below. |
| tracks | [Array](../../../../GML_Overview/Arrays.md) of [Sequence Track Struct](The_Track_Struct.md)s | This property allows access to the list of tracks which are children of this track. When getting this property an [array](../../../../GML_Overview/Arrays.md) of [Sequence Track Struct](The_Track_Struct.md)s is returned, and when setting this property an array of [Sequence Track Struct](The_Track_Struct.md)s should be specified. |
| visible | [Boolean](../../../../GML_Overview/Data_Types.md) | This indicates whether this track is visible (the value is true) or not (the value is false). You can get or set this value and if a track not visible then none of its child tracks will be drawn either. |
| keyframes | [Array](../../../../GML_Overview/Arrays.md) of [Sequence Keyframe Struct](The_Keyframe_Struct.md)s | This property allows access to the list of [keyframe structs](The_Keyframe_Struct.md) for the track. When getting this property an array of keyframe structs is returned, and when setting this property an array of keyframe structs should be specified. |
| enabled | [Boolean](../../../../GML_Overview/Data_Types.md) | This indicates whether this track is enabled. If the track is an asset track it isn't drawn when disabled, if it's a parameter track the track's values aren't applied. |

 
## Type

The type property can be any one of the following constants (these constants are also used when generating [keyframes](../sequence_keyframe_new.md) and [keyframe data](../sequence_keyframedata_new.md)):

| [Sequence Track Type Constant](The_Track_Struct.md#type) | | |
| --- | --- | --- |
| Constant | Description | Value |
| seqtracktype\_graphic | This is a graphics (sprite) asset track. | 1 |
| seqtracktype\_audio | This is an audio asset track. | 2 |
| seqtracktype\_instance | This is an instance asset track. | 14 |
| seqtracktype\_sequence | This is a sequence asset track. | 7 |
| seqtracktype\_clipmask | This is a clip mask group asset track. | 8 |
| seqtracktype\_clipmask\_mask | This is a clip mask sprite asset track used for generating the clip mask. | 9 |
| seqtracktype\_clipmask\_subject | This is a clip mask sprite asset track that is being masked. | 10 |
| seqtracktype\_group | This is a group folder asset track. | 11 |
| seqtracktype\_colour | This is a colour data parameter track. | 4 |
| seqtracktype\_real | This is a real number parameter track. | 3 |
| seqtracktype\_message | This is a broadcast message track. | 15 |
| seqtracktype\_moment | This is an event/moment track. | 16 |
| seqtracktype\_text | This is a text asset track. | 17 |
| seqtracktype\_particlesystem | This is a particle system asset track. | 18 |
| seqtracktype\_bool | Not used currently. | 5 |
| seqtracktype\_string | Not used currently. | 6 |
| seqtracktype\_spriteframes | Not used currently. | 13 |
| seqtracktype\_empty | Not used currently. | 12 |
| seqtracktype\_audioeffect | This is an audio effect parameter track. | 19 |

## Name

The name property can be any of the following strings:

- "**position**" \- when set on a track which is of type seqtracktype\_real this indicates that the contents of this track should be used as positional data.
- "**scale**" \- when set on a track which is of type seqtracktype\_real this indicates that the contents of this track should be used as scaling data.
- "**rotation**" \- when set on a track which is of type seqtracktype\_real this indicates that the contents of this track should be used as rotation data.
- "**blend\_multiply**" or "**image\_blend**" \- when set on a track which is of type seqtracktype\_colour this indicates that the contents of this track should be used as colour multiplication data. The keyframe data for such a track should be an array of four values with the format \[A, R, G, B]. Note that the values for each component are expressed as between 0 and 1, where 0 corresponds to the HEX value \#00 and 1 corresponds to the HEX value \#FF (0 \- 255 as shown in the colour picker for image blend tracks in [The Sequence Editor](../../../../../The_Asset_Editors/Sequences.md)).
- "**image\_speed**" \- when set on a track which is of type seqtracktype\_real this indicates that the contents of this track should be used as the image speed value.
- "**image\_index**" \- when set on a track which is of type seqtracktype\_real this indicates that the contents of this track should be used as the image index value.
- "**image\_angle**" \- when set on a track which is of type seqtracktype\_real this indicates that the contents of this track should be used as the image angle value.

### Text Track parameter names (only used under Text tracks)

- "**frameSize**" \- when set on a seqtracktype\_real track, this indicates that the contents of this track should be used as the frame size for the text. Each keyframe for this track should have two channels, 0 and 1, where 0 stores the X size and 1 stores the Y size of the frame.
- "**characterSpacing**" \- also used with seqtracktype\_real tracks, used as the character spacing for the text. Each keyframe for this track should have a single channel containing the spacing value.
- "**lineSpacing**" \- also used with seqtracktype\_real tracks, used as the line spacing for the text. Each keyframe for this track should have a single channel containing the spacing value.
- "**paragraphSpacing**" \- also used with seqtracktype\_real tracks, used as the paragraph spacing for the text. Each keyframe for this track should have a single channel containing the spacing value.

### Audio Effect Track parameter names

- **"audioEffect\_bus"** \- A track through which you can access and modify the properties of the [AudioBus Struct](../../Audio/Audio_Effects/AudioBus.md) that's created for this audio track's effects. It doesn't include the bus's audio effects, as each of them goes on a separate parameter track.
- **"audioEffect\_bitcrusher"** \- A track for a [Distortion (AudioEffectType.Bitcrusher)](../../Audio/Audio_Effects/AudioEffect.md#distortion) effect.
- **"audioEffect\_compressor"** \- A track for a [Compressor (AudioEffectType.Compressor)](../../Audio/Audio_Effects/AudioEffect.md#h) effect.
- **"audioEffect\_delay"** \- A track for a [Delay (AudioEffectType.Delay)](../../Audio/Audio_Effects/AudioEffect.md#delay) effect.
- **"audioEffect\_gain"** \- A track for a [Gain (AudioEffectType.Gain)](../../Audio/Audio_Effects/AudioEffect.md#gain) effect.
- **"audioEffect\_hishelf"** \- A track for a [HiShelf (AudioEffectType.HiShelf)](../../Audio/Audio_Effects/AudioEffect.md#hishelf) effect.
- **"audioEffect\_hpf2"** \- A track for a [HPF (AudioEffectType.HPF2\)](../../Audio/Audio_Effects/AudioEffect.md#hpf) effect.
- **"audioEffect\_loshelf"** \- A track for a [LoShelf (AudioEffectType.LoShelf)](../../Audio/Audio_Effects/AudioEffect.md#loshelf) effect.
- **"audioEffect\_lpf2"** \- A track for a [LPF (AudioEffectType.LPF2\)](../../Audio/Audio_Effects/AudioEffect.md#lpf) effect.
- **"audioEffect\_peakeq"** \- A track for a [PeakEQ (AudioEffectType.PeakEQ)](../../Audio/Audio_Effects/AudioEffect.md#peakeq) effect.
- **"audioEffect\_reverb1"** \- A track for a [Reverb (AudioEffectType.Reverb1\)](../../Audio/Audio_Effects/AudioEffect.md#reverb) effect.
- **"audioEffect\_tremolo"** \- A track for a [Tremolo (AudioEffectType.Tremolo)](../../Audio/Audio_Effects/AudioEffect.md#tremolo) effect.

## Interpolation

The interpolation property can take one of the following constants: 

| [Sequence Track Interpolation Constant](The_Track_Struct.md#interpolation) | | |
| --- | --- | --- |
| Constant | Description | Value |
| seqinterpolation\_assign | Don't use interpolation for this track | 0 |
| seqinterpolation\_lerp | Use linear interpolation for this track | 1 |
