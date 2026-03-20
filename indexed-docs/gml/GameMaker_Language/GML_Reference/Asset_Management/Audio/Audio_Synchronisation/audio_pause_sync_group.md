# audio\_pause\_sync\_group

This function will pause the given sync group if it is playing, with the group index being the value returned when you created the group using the function [audio\_create\_sync\_group()](audio_create_sync_group.md). This does not stop the sound, and calling [audio\_resume\_sync\_group()](audio_resume_sync_group.md), will start it playing from the same position it was paused at again.

 
 

#### Syntax:

audio\_pause\_sync\_group(group\_index)

| Argument | Type | Description |
| --- | --- | --- |
| group\_index | [Audio Sync Group ID](audio_create_sync_group.md) | The group index to pause. |

 

#### Returns:

N/A

 

#### Example:

if (keyboard\_check\_pressed((ord)"P"))  

 {  

     global.Pause \= !global.Pause  

     if (global.Pause)  

     {  

         audio\_pause\_sync\_group(sg);  

     }  

     else  

     {  

         audio\_resume\_sync\_group(sg);  

     }  

 }

The above code checks for a key press of the "P" key, and if one is detected it toggles the "global.Pause" variable then checks it to pause or resume the sync group indexed in the variable "sg".
