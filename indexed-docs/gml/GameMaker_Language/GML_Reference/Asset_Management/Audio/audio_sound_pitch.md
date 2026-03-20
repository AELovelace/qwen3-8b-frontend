# audio\_sound\_pitch

This function changes the pitch of the given sound asset or instance.

The sound can either be one referenced from an index for an individual sound being played which has been stored in a variable when using the [audio\_play\_sound()](audio_play_sound.md) or [audio\_play\_sound\_at()](audio_play_sound_at.md) functions, or an actual sound asset from the Asset Browser. If it is an index of a playing sound, that sound instance's pitch will be changed. When using a sound asset from the Asset Browser, however, the sound asset's pitch is changed which will give an audible change in the pitch of all instances of that sound asset being played.

The pitch argument is a *pitch multiplier*, in that the input value multiplies the current pitch by that amount, so the default value of 1 is no pitch change, while a value of less than 1 will lower the pitch and greater than 1 will raise the pitch. It is best to use small increments for this function as any value under 0 or over 5 may not be audible anyway. It is worth noting that the total pitch change permitted is clamped to (1/256) \- 256 octaves, so any value over or under this will not be registered.

The clamped value given above is what GameMaker attempts to clamp the range to, but this value is **not** guaranteed on all target platforms. iOS, for example, clamps to (1/256) \- 8, so you may need to experiment on each target platform and have different versions of a sound resource, each one pre\-shifted, should you require higher or lower octave values.

 
#### Syntax:

audio\_sound\_pitch(index, pitch)

| Argument | Type | Description |
| --- | --- | --- |
| index | [Sound Asset](../../../../The_Asset_Editors/Sounds.md) or [Sound Instance ID](audio_play_sound.md) or [Audio Queue ID](Audio_Buffers/audio_create_play_queue.md) | The index of the sound to change. |
| pitch | [Real](../../../GML_Overview/Data_Types.md) |  |

 

#### Returns:

N/A

 

#### Example:

var s\_engine \= audio\_play\_sound(snd\_CarEngine, 10, false);  

 switch (gear)  

 {  

     case 1: audio\_sound\_pitch(s\_engine, 0\.8\); break;  

     case 2: audio\_sound\_pitch(s\_engine, 0\.9\); break;  

     case 3: audio\_sound\_pitch(s\_engine, 0\.95\); break;  

     case 4: audio\_sound\_pitch(s\_engine, 1\); break;  

     case 5: audio\_sound\_pitch(s\_engine, 1\.2\); break;  

 }

The above code will change the pitch of the audio played from the sound indexed in the variable "s\_engine" based on the value of the variable "gear".
