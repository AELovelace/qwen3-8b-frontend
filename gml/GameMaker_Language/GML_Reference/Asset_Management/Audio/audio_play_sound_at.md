# audio\_play\_sound\_at

With this function you can play any sound asset at a given position within the audio space.

 
You provide the sound index and then assign it a position within the 3D space. The default listener position is (0, 0, 0\) so this means that if the listener has not been moved and you want the sound to come from the left (for example), you should set the x position to a negative value (for more information on setting the listener position see [audio\_listener\_position()](Audio_Listeners/audio_listener_position.md)).

You can also set a fall\-off distance (0 will make the sound silent, default is 100\) which will make the sound fade out as it gets further from the listener position. How the fade itself is heard will depend on the falloff reference (which is the distance under which the volume for the source would normally drop by half) and the roll off factor (which affects the sound past the falloff reference distance only). The default factor is normally 1, and the effect of the different falloff values will depend on the model chosen (for a complete guide to the different falloff models and how these values are used, please see the function [audio\_falloff\_set\_model()](audio_falloff_set_model.md)).

The next two arguments are to set the sound is to loop or not and for assigning a priority to the sound. This priority is then used to determine how sounds are dealt with when the number of sounds playing is over the limit set by the function [audio\_channel\_num()](audio_channel_num.md). Lower priority sounds will be stopped in favour of higher priority sounds, and the priority value can be any real number (the actual value is arbitrary, and can be from 0 to 1 or 0 to 100, as GameMaker will prioritise them the same). Note that when dealing with priority, the *higher* the number the *higher* the priority, such that a sound with priority 100 will be favoured over a sound with priority 1\.

This function will also return a unique index for the sound being played, which can be stored in a variable so you can later [pause it](audio_pause_sound.md) or [stop it](audio_stop_sound.md). This means that if you have multiple instances of the same sound playing at any one time, you can target just one instance of that sound using the [audio functions](Audio.md).

 
 

#### Syntax:

audio\_play\_sound\_at(index, x, y, z, falloff\_ref, falloff\_max, falloff\_factor, loop, priority, \[gain], \[offset], \[pitch], \[listener\_mask])

| Argument | Type | Description |
| --- | --- | --- |
| index | [Sound Asset](../../../../The_Asset_Editors/Sounds.md) or [Audio Queue ID](Audio_Buffers/audio_create_play_queue.md) | The index of the sound to play. |
| x | [Real](../../../GML_Overview/Data_Types.md) | The x position. |
| y | [Real](../../../GML_Overview/Data_Types.md) | The y position. |
| z | [Real](../../../GML_Overview/Data_Types.md) | The z position. |
| falloff\_ref | [Real](../../../GML_Overview/Data_Types.md) | The falloff reference relative to the listener (clamp). |
| falloff\_max | [Real](../../../GML_Overview/Data_Types.md) | The maximum falloff distance relative to the listener. |
| falloff\_factor | [Real](../../../GML_Overview/Data_Types.md) | The falloff factor (default 1\). |
| loop | [Boolean](../../../GML_Overview/Data_Types.md) | Flags the sound as looping or not. |
| priority | [Real](../../../GML_Overview/Data_Types.md) | Set the channel priority for the sound. |
| gain | [Real](../../../GML_Overview/Data_Types.md) | The gain of the sound instance (defaults to 1\). |
| offset | [Real](../../../GML_Overview/Data_Types.md) | The time (in seconds) to start playing. Values beyond the end of the sound are clamped to its length. The default value is the asset\-level offset. |
| pitch | [Real](../../../GML_Overview/Data_Types.md) |  |
| listener\_mask | [Real](../../../GML_Overview/Data_Types.md) | The bitmask data to set for the sound. On the HTML5 target  this will have no effect as the target does not support more than one listener. |

 

#### Returns:

[Sound Instance ID](audio_play_sound.md) (or \-1 if the sound could not be played)

 

#### Example 1:

if (global.SFX)  

 {  

     audio\_play\_sound\_at(snd\_Waterfall, x, y, 0, 100, 300, 1, true, 1\);  

 }

The above code checks the global variable "SFX" and if it returns true then the sound indexed in the variable "snd\_Waterfall" will be looped at its room position, with a fall\-off reference of 100, a falloff distance of 300, a falloff factor of 1 and a low priority.

#### Example 2:

if (global.SFX)  

 {  

     audio\_play\_sound\_at(snd\_Waterfall, x, y, 0, 100, 300, 1, true, 1, 1, 2\);  

 }

The above code checks the global variable "SFX" and if it returns true then the sound indexed in the variable "snd\_Waterfall" will be looped at its room position using the given falloff settings and no change in gain. The sound immediately starts playing from second 2\.
