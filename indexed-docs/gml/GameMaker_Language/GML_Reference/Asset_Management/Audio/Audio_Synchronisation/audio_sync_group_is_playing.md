# audio\_sync\_group\_is\_playing

This function can be used to check if any audio in a synchronised group is playing. You are required to supply the sync group ID as returned by the function [audio\_create\_sync\_group()](audio_create_sync_group.md).

 
 

#### Syntax:

audio\_sync\_group\_is\_playing(group\_index)

| Argument | Type | Description |
| --- | --- | --- |
| group\_index | [Audio Sync Group ID](../../../../../../GameMaker_Language/GML_Reference/Asset_Management/Audio/Audio_Synchronisation/audio_create_sync_group.md) | The group index to check. |

 

#### Returns:

[Boolean](../../../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

if audio\_sync\_group\_is\_playing(group\_one)  

 {  

     audio\_stop\_sync\_group(group\_one);  

 }

The above code checks to see if the sync group group\_one is currently playing and if it is, the group is stopped.
