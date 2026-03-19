# audio\_group\_is\_loaded

This function will check a specific audio group to see if it has been loaded into memory, ready for use.

 

#### Syntax:

audio\_group\_is\_loaded(groupID)

| Argument | Type | Description |
| --- | --- | --- |
| groupID | [Audio Group ID](../../../../../../GameMaker_Language/GML_Reference/Asset_Management/Audio/Audio_Groups/Audio_Groups.md) | The index of the audio group to check (as defined in the [Audio Groups](../../../../../Settings/Audio_Groups.md) window) |

 

#### Returns:

[Boolean](../../../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

if audio\_group\_is\_loaded(audiogroup\_level1\)  

 {  

     audio\_group\_unload(audiogroup\_level1\);  

 }

The above code checks to see if an audio group has been loaded and if it has it unloads it.
