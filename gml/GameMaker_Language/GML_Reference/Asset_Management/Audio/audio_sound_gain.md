# audio\_sound\_gain

With this function you can fade a sound asset or instance in or out over a given length of time, or it can be used to set the sound gain instantly.

 
The time is measured in milliseconds, and the function requires that you input a final level of gain for the sound to have reached by the end of that time. This gain can be between 0 (silent) and any value greater than 0, although normally you'd consider the maximum volume as 1\. Anything over 1 can be used but, depending on the sound used and the platform being compiled to, you may get distortion or clipping when the sound is played back. Note that the gain scale is linear, and to instantly change the gain, simply leave out the time argument or set it to 0\.

 
This function will affect *all* instances of the sound that are playing currently in the room if the index is a sound asset, and the final volume will be the volume at which all further instances of the sound will be played. However, if you have used the index returned from a function like [audio\_play\_sound](audio_play_sound.md) it will only affect that one instance of the sound.

 
 

#### Syntax:

audio\_sound\_gain(index, volume, \[time])

| Argument | Type | Description |
| --- | --- | --- |
| index | [Sound Asset](../../../../The_Asset_Editors/Sounds.md) or [Sound Instance ID](audio_play_sound.md) or [Audio Queue ID](Audio_Buffers/audio_create_play_queue.md) | The index of the sound to set the gain for. |
| volume | [Real](../../../GML_Overview/Data_Types.md) | The new linear gain value. |
| time | [Real](../../../GML_Overview/Data_Types.md) | The length for the change in gain in milliseconds. Defaults to 0 (instantaneous change) if not passed. |

 

#### Returns:

N/A

 

#### Example 1:

var \_snd \= audio\_play\_sound(snd\_fountain, 10, true);  

audio\_sound\_gain(\_snd, 0, 0\);  

audio\_sound\_gain(\_snd, 1, 5000\);
 

The above code assigns the index of a sound to be played to the local variable snd. This variable is then used to reduce the volume of that specific sound to 0 and fade up to full volume over 5 seconds.

 

#### Example 2:

audio\_sound\_gain(snd\_fountain, 0\.5\);  

 var \_snd \= audio\_play\_sound(snd\_fountain, 0, true, 2\);

The above code first sets the gain of the sound asset snd\_fountain to 0\.5\. It then plays this sound using [audio\_play\_sound](audio_play_sound.md) and sets the gain of this new sound instance to 2 (using the optional "gain" parameter of the function).
