# audio\_sound\_get\_pitch

This function can be used to get the pitch of a given sound.

The sound can either be one referenced from an index for an individual sound being played which has been stored in a variable when using the [audio\_play\_sound()](audio_play_sound.md) or [audio\_play\_sound\_at()](audio_play_sound_at.md) functions, or an actual sound asset from [The Asset Browser](../../../../Introduction/The_Asset_Browser.md).

 

#### Syntax:

audio\_sound\_get\_pitch(index)

| Argument | Type | Description |
| --- | --- | --- |
| index | [Sound Asset](../../../../The_Asset_Editors/Sounds.md) or [Sound Instance ID](audio_play_sound.md) or [Audio Queue ID](Audio_Buffers/audio_create_play_queue.md) | The index of the sound to get the pitch of. |

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

if audio\_sound\_get\_pitch(snd\_Explode) !\= 1  

 {  

     audio\_sound\_pitch(snd\_Explode, 1\);  

 }

The above code will change the pitch of the audio played from the sound indexed as "snd\_Explode" if its pitch is not equal to 1\.
