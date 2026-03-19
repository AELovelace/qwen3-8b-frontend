# instance\_deactivate\_object

With this function you can deactivate a single instance or all instances of a specific object from all those that have been activated previously. Note that if you have deactivated an instance or object that has been flagged as **Persistent**, then you will need to reactivate it again with the function [instance\_activate\_object](instance_activate_object.md) before changing room, otherwise it will *not* be carried over and will be discarded instead. Note too that deactivation is not instantaneous, and an instance that has been deactivated in this way will not be considered to be inactive until the end of the event in which the function was called.

 
 
 
 

#### Syntax:

instance\_deactivate\_object(obj, \[collision\_space])

| Argument | Type | Description |
| --- | --- | --- |
| obj | [Object Asset](../../../../../The_Asset_Editors/Objects.md) or [Object Instance](../Instance_Variables/id.md) | The object or instance to deactivate (the keyword **all** can also be used). |
| collision\_space | [Collision Space](../Instance_Variables/collision_space.md) | The collision space where instances will be deactivated |

 

#### Returns:

N/A

 

#### Example:

instance\_deactivate\_object(obj\_Enemy);  

 var \_vx \= camera\_get\_view\_x(view\_camera\[0]);  

 var \_vy \= camera\_get\_view\_y(view\_camera\[0]);  

 var \_vw \= camera\_get\_view\_width(view\_camera\[0]);  

 var \_vh \= camera\_get\_view\_height(view\_camera\[0]);  

 instance\_activate\_region(\_vx \- 64, \_vy \- 64, \_vw \+ 128, \_vh \+ 128, false);

The above code deactivates all instances of the object "obj\_Enemy" and then activates a region within the room.
