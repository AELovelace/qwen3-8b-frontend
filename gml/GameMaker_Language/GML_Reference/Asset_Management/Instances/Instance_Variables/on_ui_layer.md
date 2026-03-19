# on\_ui\_layer

This **built\-in variable** is created for every instance in a room and stores whether the instance is placed on a [UI layer](../../../../../The_Asset_Editors/Room_Properties/UI_Layers.md) (true) or not (false). You can check the specific type of UI layer by calling [collision\_space](collision_space.md).

 

#### Syntax:

on\_ui\_layer

 

#### Returns:

[Boolean](../../../../GML_Overview/Data_Types.md)

 

#### Example:

with (all)  

 {  

     if (!on\_ui\_layer) depth \= \-bbox\_bottom;  

 }

This runs a line of code for all instances in the room. If the instance is not on a UI layer, its depth is set to its bottom bounding box edge.
