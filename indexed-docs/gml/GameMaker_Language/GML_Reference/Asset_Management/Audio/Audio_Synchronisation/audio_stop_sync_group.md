# audio\_stop\_sync\_group

This function will stop the given sync group if it is playing, with the group index being the value returned when you created the group using the function [audio\_create\_sync\_group()](audio_create_sync_group.md).

 
 

#### Syntax:

audio\_stop\_sync\_group(group\_index)

| Argument | Type | Description |
| --- | --- | --- |
| group\_index | [Audio Sync Group ID](../../../../../../GameMaker_Language/GML_Reference/Asset_Management/Audio/Audio_Synchronisation/audio_create_sync_group.md) | The group index to stop playing. |

 

#### Returns:

N/A

 

#### Example:

if (mouse\_check\_button\_pressed(mb\_left))   

 {  

     audio\_stop\_sync\_group(sg);  

 }

The above code checks for a mouse click, and if one is detected it stops the sync group indexed in the variable "sg".
