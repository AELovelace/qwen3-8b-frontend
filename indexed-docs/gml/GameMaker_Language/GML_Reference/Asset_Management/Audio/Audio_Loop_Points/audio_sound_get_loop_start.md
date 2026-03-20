# audio\_sound\_get\_loop\_start

This function returns the loop [start point](audio_sound_loop_start.md) in seconds for the given sound asset or sound instance.

  

#### Syntax:

audio\_sound\_get\_loop\_start(index)

| Argument | Type | Description |
| --- | --- | --- |
| index | [Sound Asset](../../../../../../The_Asset_Editors/Sounds.md) or [Sound Instance ID](../../../../../../GameMaker_Language/GML_Reference/Asset_Management/Audio/audio_play_sound.md) | The ID of a sound asset or a sound instance |

 

#### Returns:

[Real](../../../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

var \_loop\_start\_time \= audio\_sound\_get\_loop\_start(snd\_loop);

The above code calls audio\_sound\_get\_loop\_start on an existing sound asset snd\_loop and stores the returned value in a variable \_loop\_start\_time.
