# audio\_sound\_get\_audio\_group

This function returns the ID of the [audio group](../../../../../Settings/Audio_Groups.md) the given sound asset or sound instance belongs to.

 

#### Syntax:

audio\_sound\_get\_audio\_group(sound\_index)

| Argument | Type | Description |
| --- | --- | --- |
| sound\_index | [Sound Asset](../../../../../../The_Asset_Editors/Sounds.md) or [Sound Instance ID](../../../../../../GameMaker_Language/GML_Reference/Asset_Management/Audio/audio_play_sound.md) | The index of a sound asset or instance |

 

#### Returns:

[Audio Group ID](../../../../../../GameMaker_Language/GML_Reference/Asset_Management/Audio/Audio_Groups/Audio_Groups.md)

 

#### Example:

var \_group \= audio\_sound\_get\_audio\_group(snd\_animal);

The above code gets the ID of the audio group assigned to the sound snd\_animal and stores it in a temporary variable \_group.
