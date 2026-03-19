# audio\_sync\_group\_get\_track\_pos

This function returns the current play position of the given sync group. The group index is the value returned when you created the group using the function [audio\_create\_sync\_group()](audio_create_sync_group.md), and the return value is the time in seconds that the tracks have been playing.

 
 

#### Syntax:

audio\_sync\_group\_get\_track\_pos(group\_index)

| Argument | Type | Description |
| --- | --- | --- |
| group\_index | [Audio Sync Group ID](../../../../../../GameMaker_Language/GML_Reference/Asset_Management/Audio/Audio_Synchronisation/audio_create_sync_group.md) | The group index to get the position of. |

 

#### Returns:

[Real](../../../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

var real\_secs \= audio\_sync\_group\_get\_track\_pos(sg);  

 var secs \= real\_secs mod 60;  

 var mins \= string(real\_secs div 60\);  

 if (secs \> 9\)  

 {  

     secs \= string(secs);  

 }  

 else  

 {  

     secs \= "0" \+ string(secs);  

 }  

  

 draw\_text(32, 32, "Time \= " \+ mins \+ ":" \+ secs);
 

The above code gets the time position for the sync group indexed in the variable "sg", then uses this value to draw the time played on the screen.
