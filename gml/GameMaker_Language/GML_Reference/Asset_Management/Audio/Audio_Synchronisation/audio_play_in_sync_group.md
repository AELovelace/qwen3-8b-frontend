# audio\_play\_in\_sync\_group

With this function you can assign a sound to a previously created sync group. The group index is the value returned when you created the group using the function [audio\_create\_sync\_group()](audio_create_sync_group.md), and the sound index is the handle of any sound from the Asset Browser. This function only adds the sound to the group, but it does not play the sound. The return value will be \>\= 0 if it succeeds and \-1 if it fails, where a successful value indicates the sound's order in the sync group (so 0 would be the first sound added, 1 would be the second, etc.). 

 
 

#### Syntax:

audio\_play\_in\_sync\_group(group\_index, sound\_index)

| Argument | Type | Description |
| --- | --- | --- |
| group\_index | [Audio Sync Group ID](audio_create_sync_group.md) | The group index to assign the sound to. |
| sound\_index | [Sound Asset](../../../../../The_Asset_Editors/Sounds.md) | The sound index to be assigned to the group. |

 

#### Returns:

[Real](../../../../GML_Overview/Data_Types.md)

 

#### Example:

sg \= audio\_create\_sync\_group(true);  

 audio\_play\_in\_sync\_group(sg, sound1\);  

 audio\_play\_in\_sync\_group(sg, sound2\);  

 audio\_play\_in\_sync\_group(sg, sound3\);  

 audio\_play\_in\_sync\_group(sg, sound4\);  

 audio\_start\_sync\_group(sg);

The above creates a new sync group and assigns the index of the group to the variable "sg". Four sounds are then added to the group, with the gain for three of them being set to 0\. Finally the sync group is played.
