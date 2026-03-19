# audio\_sound\_get\_loop

This function returns whether the given sound instance being played is set to loop.

 

#### Syntax:

audio\_sound\_get\_loop(index)

| Argument | Type | Description |
| --- | --- | --- |
| index | [Sound Instance ID](../../../../../../GameMaker_Language/GML_Reference/Asset_Management/Audio/audio_play_sound.md) | The index of the sound instance |

 

#### Returns:

[Boolean](../../../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

var \_loop \= audio\_sound\_get\_loop(snd\_car);

The above code calls audio\_sound\_get\_loop on an existing sound asset snd\_car and stores the result in a temporary variable \_loop.
