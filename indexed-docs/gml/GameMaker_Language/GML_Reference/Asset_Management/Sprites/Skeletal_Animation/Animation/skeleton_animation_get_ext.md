# skeleton\_animation\_get\_ext

This function will return the name of the animation set currently used by the given track number (as set by the function [skeleton\_animation\_set\_ext](skeleton_animation_set_ext.md)).

A single skeletal animation sprite can have various animation sets, and these sets can be assigned different tracks so that you can "mix and match" animation sets.

 

#### Syntax:

skeleton\_animation\_get\_ext(track)

| Argument | Type | Description |
| --- | --- | --- |
| track | [Real](../../../../../GML_Overview/Data_Types.md) | The track number to get the animation set name of. |

 

 

#### Returns:

[String](../../../../../GML_Overview/Data_Types.md)

 

#### Example:

if (skeleton\_animation\_get\_ext(1\) !\= "bodyfight")  

 {  

     skeleton\_animation\_set\_ext("bodyfight", 1\);  

 }

The above code will change the animation set being used by track 1 to "bodyfight" if it is not already.
