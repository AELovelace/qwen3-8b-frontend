# audio\_group\_load\_progress

This function will check the loading progress for an audio group and return an (approximate) value between 0 and 100\.

 

#### Syntax:

audio\_group\_load\_progress(groupID)

| Argument | Type | Description |
| --- | --- | --- |
| groupID | [Audio Group ID](../../../../../../GameMaker_Language/GML_Reference/Asset_Management/Audio/Audio_Groups/Audio_Groups.md) | The index of the audio group to check (as defined in the [Audio Groups](../../../../../Settings/Audio_Groups.md) window) |

 

#### Returns:

[Real](../../../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

if (load)   

 {  

     var pc \= audio\_group\_load\_progress(audiogroup\_level1\);  

     draw\_text(32, 32, "Loading: " \+ string(pc));  

 }

The above code checks a variable and if it returns true then some text will be drawn showing the progress of the audio being loaded.
