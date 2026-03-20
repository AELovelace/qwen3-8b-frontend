# visible

An instance can be flagged as *visible* or not by setting this variable to true (visible) or false (invisible).

This works by telling GameMaker to skip [Draw Events](../../../../../The_Asset_Editors/Object_Properties/Draw_Events.md) for this instance, so care must be taken when using this as it means that no code placed in any of the Draw events will be run while the instance is not visible. Also note that if the [layer](layer.md) that the instance is assigned to is [flagged as invisible](../../Rooms/General_Layer_Functions/layer_set_visible.md "layer_set_visible()"), setting this variable to true will have no effect until the layer itself is flagged as visible too.

  During Draw events, this variable will become **read\-only** and attempting to change it will throw a fatal error.

 

#### Syntax:

visible

 

#### Returns:

[Boolean](../../../../GML_Overview/Data_Types.md)

 

#### Example:

if (other.visible)  

 {  

     x \= xprevious;  

     y \= yprevious;  

 }

The above code will check the visible flag of the "other" instance in a *Collision event* and if it is set to true, it will move the current instance back to its previous position.
