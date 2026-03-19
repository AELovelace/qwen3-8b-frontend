# instance\_deactivate\_layer

With this function you can deactivate all instances assigned to a specific layer. You need to supply the **layer handle**, which can either be the name of the layer as written in the code editor (as a string) or the actual layer handle value as returned by [layer\_create](../../Rooms/General_Layer_Functions/layer_create.md), and note that you can only deactivate *instance* layers with this function. Note that if you have deactivated a layer that has instances of objects flagged as **Persistent**, then you will need to reactivate the layer again with the function [instance\_activate\_layer](instance_activate_layer.md) before changing room, otherwise any persistent instances on the layer will *not* be carried over and will be discarded. Note too that deactivation is not instantaneous, and an instance that has been deactivated in this way will not be considered to be inactive until the end of the event in which the function was called.

 
 
 

#### Syntax:

instance\_deactivate\_layer(obj)

| Argument | Type | Description |
| --- | --- | --- |
| layer | [Layer](../../Rooms/General_Layer_Functions/layer_get_id.md) or [String](../../../../GML_Overview/Data_Types.md) | The layer name string (or handle) to be used |

 

#### Returns:

N/A

 

#### Example:

instance\_deactivate\_layer("Enemy Layer");  

 var \_vx \= camera\_get\_view\_x(view\_camera\[0]);  

 var \_vy \= camera\_get\_view\_y(view\_camera\[0]);  

 var \_vw \= camera\_get\_view\_width(view\_camera\[0]);  

 var \_vh \= camera\_get\_view\_height(view\_camera\[0]);  

 instance\_activate\_region(\_vx \- 64, \_vy \- 64, \_vw \+ 128, \_vh \+ 128, false);

The above code deactivates all instances assigned to the layer "Enemy Layer" and then activates a region within the room.
