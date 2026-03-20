# audio\_group\_get\_assets

This function returns an array containing the sound asset IDs belonging to the [audio group](../../../../../Settings/Audio_Groups.md) with the given ID.

 

#### Syntax:

audio\_group\_get\_assets(group\_index)

| Argument | Type | Description |
| --- | --- | --- |
| group\_index | [Audio Group ID](../../../../../../GameMaker_Language/GML_Reference/Asset_Management/Audio/Audio_Groups/Audio_Groups.md) | The index of the audio group |

 

#### Returns:

[Array](../../../../../../GameMaker_Language/GML_Overview/Arrays.md) of [Sound Asset](../../../../../../The_Asset_Editors/Sounds.md)

 

#### Example:

var \_assets \= audio\_group\_get\_assets(audiogroup\_default);

In the above code, an array containing all asset IDs in the default audio group [audiogroup\_default](audiogroup_default.md) is returned by a call to audio\_group\_get\_assets and stored in a temporary variable \_assets.
