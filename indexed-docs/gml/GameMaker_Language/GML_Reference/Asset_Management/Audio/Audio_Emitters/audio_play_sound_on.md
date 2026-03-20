# audio\_play\_sound\_on

This function plays any sound asset through an emitter, with any changes to the emitter's gain, position, pitch or velocity affecting how the user hears the final sound being played.

 
You provide the emitter index to use, the [Sound Asset](../../../../../The_Asset_Editors/Sounds.md) to be played and then specify whether the sound is to loop or not. Next you can assign a priority, which is then used to determine how sounds are dealt with when the number of sounds playing is over the limit set by the function [audio\_channel\_num()](../audio_channel_num.md). Lower priority sounds will be stopped in favour of higher priority sounds, and the priority value can be any real number (the actual value is arbitrary, and can be from 0 to 1 or 0 to 100, as GameMaker will prioritise them the same). Note that when dealing with priority, the *higher* the number the *higher* the priority, such that a sound with priority 100 will be favoured over a sound with priority 1\.

This function will also return a unique index for the sound being played, which can be stored in a variable so you can later [pause it](../audio_pause_sound.md) or [stop it](../audio_stop_sound.md). This means that if you have multiple instances of the same sound playing at any one time, you can target just one instance of that sound using the [audio functions](../Audio.md).

 
 

#### Syntax:

audio\_play\_sound\_on(emitter, sound, loop, priority, \[gain], \[offset], \[pitch], \[listener\_mask])

| Argument | Type | Description |
| --- | --- | --- |
| emitter | [Audio Emitter ID](audio_emitter_create.md) | The index of the emitter to use. |
| sound | [Sound Asset](../../../../../The_Asset_Editors/Sounds.md) | The index of the sound to use. |
| loop | [Boolean](../../../../GML_Overview/Data_Types.md) | Flags the sound as looping or not. |
| priority | [Real](../../../../GML_Overview/Data_Types.md) | Set the channel priority for the sound. |
| gain | [Real](../../../../GML_Overview/Data_Types.md) | The gain of the sound instance (defaults to 1\). |
| offset | [Real](../../../../GML_Overview/Data_Types.md) | The time (in seconds) to start playing. Values beyond the end of the sound are clamped to its length. The default value is the asset\-level offset. |
| pitch | [Real](../../../../GML_Overview/Data_Types.md) |  |
| listener\_mask | [Real](../../../../GML_Overview/Data_Types.md) | The bitmask data to set for the sound. On the HTML5 target this will have no effect as the target does not support more than one listener. |

 

#### Returns:

[Sound Instance ID](../audio_play_sound.md) (or \-1 if the sound could not be played)

 

#### Example 1:

if (global.SFX)  

 {  

     audio\_play\_sound\_on(s\_emit, snd\_Explode, false, 1\);  

 }

The above code checks the global variable "SFX" and if it returns true then the sound indexed in the variable "snd\_Explode" will be played through the emitter indexed in the variable "s\_emit" with a low priority and no looping.

#### Example 2:

if (hit \=\= true)  

 {  

     audio\_play\_sound\_on(s\_emit, snd\_Hit, false, 1, 1\.3\);  

 }

The above code checks if the instance executing the code was hit. If true it plays the sound "snd\_Hit" through the emitter "s\_emit" with a slightly higher gain of 1\.3\. The gain set here is multiplied by the emitter's gain to get the final gain at which the sound is played.
