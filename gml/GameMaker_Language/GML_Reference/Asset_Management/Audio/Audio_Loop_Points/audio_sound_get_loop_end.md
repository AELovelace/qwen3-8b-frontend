# audio\_sound\_get\_loop\_end

This function returns the loop [end point](audio_sound_loop_end.md) in seconds for the given sound asset or sound instance.

  

#### Syntax:

audio\_sound\_get\_loop\_end(index)

| Argument | Type | Description |
| --- | --- | --- |
| index | [Sound Asset](../../../../../../The_Asset_Editors/Sounds.md) or [Sound Instance ID](../../../../../../GameMaker_Language/GML_Reference/Asset_Management/Audio/audio_play_sound.md) | The index of the sound asset or instance |

 

#### Returns:

[Real](../../../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

var \_loop\_end\_time \= audio\_sound\_get\_loop\_end(snd\_loop);

The above code calls audio\_sound\_get\_loop\_end on an existing sound asset snd\_loop and stores the returned value in a variable \_loop\_end\_time.
