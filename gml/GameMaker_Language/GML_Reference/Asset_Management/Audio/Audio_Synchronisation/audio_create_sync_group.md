# audio\_create\_sync\_group

This function creates a sync group and returns a unique ID value for it which should then be used in all further audio function calls for this group. If you want the group to loop then pass in true, otherwise pass in false, but note that if you want them to loop, *all the tracks added later need to be the same length*. Note that when you create a sync group, you will need to free the memory and sounds associated with it when not in use using the [audio\_destroy\_sync\_group()](audio_destroy_sync_group.md) function \- for example, in the **Room End** or **Destroy** events.

 
 

#### Syntax:

audio\_create\_sync\_group(loop)

| Argument | Type | Description |
| --- | --- | --- |
| loop | [Boolean](../../../../GML_Overview/Data_Types.md) | Whether the tracks in the group should loop (true) or not (false). |

 

#### Returns:

[Audio Sync Group ID](audio_create_sync_group.md)

 

#### Example:

sg \= audio\_create\_sync\_group(true);  

 audio\_play\_in\_sync\_group(sg, sound1\);  

 audio\_play\_in\_sync\_group(sg, sound2\);  

 audio\_sound\_gain(sound2, 0, 0\);  

 audio\_play\_in\_sync\_group(sg, sound3\);  

 audio\_sound\_gain(sound3, 0, 0\);  

 audio\_play\_in\_sync\_group(sg, sound4\);  

 audio\_sound\_gain(sound4, 0, 0\);  

 audio\_start\_sync\_group(sg);

The above creates a new sync group and assigns the index of the group to the variable "sg". Four sounds are then added to the group, with the gain for three of them set to 0\. Finally the sync group is played.
