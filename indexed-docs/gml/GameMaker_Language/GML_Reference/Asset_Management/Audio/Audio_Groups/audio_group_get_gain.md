# audio\_group\_get\_gain

This function returns the gain of the audio group with the given ID.

 

#### Syntax:

audio\_group\_get\_gain(groupID)

| Argument | Type | Description |
| --- | --- | --- |
| groupID | [Audio Group ID](../../../../../../GameMaker_Language/GML_Reference/Asset_Management/Audio/Audio_Groups/Audio_Groups.md) | The ID of the audio group |

 

#### Returns:

[Real](../../../../../../GameMaker_Language/GML_Overview/Data_Types.md) (the gain of the audio group)

 

#### Example:

var \_default\_group\_gain \= audio\_group\_get\_gain(audiogroup\_default);

This gets the gain of the default audio group and stores it in a variable.
