# audio\_is\_playing

This function will check the given sound to see if it is currently playing.

The sound can either be a single instance of a sound (the index for individual sounds being played can be stored in a variable when using the [audio\_play\_sound](audio_play_sound.md), [audio\_play\_sound\_at](audio_play_sound_at.md), [audio\_play\_sound\_on](Audio_Emitters/audio_play_sound_on.md) and [audio\_play\_sound\_ext](audio_play_sound_ext.md) functions) or a sound asset, in which case *all* instances of the given sound will be checked and if any of them are playing the function will return true otherwise it will return false.

  This function will still return true if the sound being checked has previously been paused using the [audio\_pause\_sound](audio_pause_sound.md) function.

 

#### Syntax:

audio\_is\_playing(index)

| Argument | Type | Description |
| --- | --- | --- |
| index | [Sound Asset](../../../../../The_Asset_Editors/Sounds.md) or [Sound Instance ID](../../../../../GameMaker_Language/GML_Reference/Asset_Management/Audio/audio_play_sound.md) | The index of the sound to check. |

 

#### Returns:

[Boolean](../../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

if !audio\_is\_playing(snd\_Waterfall)  

 {  

     audio\_play\_sound\_at(snd\_Waterfall, x, y, 0, 300, true, 1\);  

 }

The above code checks to see if the sound indexed in the variable "snd\_Waterfall" is currently playing and if it returns false then the sound will be looped at its room position, with a fall\-off distance of 300 and a low priority.
