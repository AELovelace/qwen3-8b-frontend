# audio\_destroy\_sync\_group

Audio sync groups need to be destroyed when not in use to free up the memory and sound resources associated with them using this function. It takes the group index as returned when the group was created using the function [audio\_create\_sync\_group()](audio_create_sync_group.md), and frees all resources used by the group.

 
 

#### Syntax:

audio\_destroy\_sync\_group(group\_index)

| Argument | Type | Description |
| --- | --- | --- |
| group\_index | [Audio Sync Group ID](../../../../../../GameMaker_Language/GML_Reference/Asset_Management/Audio/Audio_Synchronisation/audio_create_sync_group.md) | The group index to be destroyed. |

 

#### Returns:

N/A

 

#### Example:

audio\_destroy\_sync\_group(sg);

The above code destroys the sync group indexed in the variable "sg", and would probably be used in the **destroy** or **Room End** events.
