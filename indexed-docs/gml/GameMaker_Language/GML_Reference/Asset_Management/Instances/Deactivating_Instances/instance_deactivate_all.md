# instance\_deactivate\_all

This function will deactivate **all** instances that are in the room at the moment that the code is run. This may include the instance running the code if the notme flag is set to false, but normally you would want that instance to be active, in which case the notme flag should be set to true. Note that deactivation is not instantaneous, and an instance that has been deactivated in this way will not be considered to be inactive until the end of the event in which the function was called.

 
 
 
 

#### Syntax:

instance\_deactivate\_all(notme, \[collision\_space])

| Argument | Type | Description |
| --- | --- | --- |
| notme | [Boolean](../../../../GML_Overview/Data_Types.md) | Whether to keep the calling instance activated (true) or not (false). |
| collision\_space | [Collision Space](../Instance_Variables/collision_space.md) | The collision space where instances will be deactivated |

 

#### Returns:

N/A

 

#### Example:

instance\_deactivate\_all(true);  

 var \_vx \= camera\_get\_view\_x(view\_camera\[0]);  

 var \_vy \= camera\_get\_view\_y(view\_camera\[0]);  

 var \_vw \= camera\_get\_view\_width(view\_camera\[0]);  

 var \_vh \= camera\_get\_view\_height(view\_camera\[0]);  

 instance\_activate\_region(\_vx \- 64, \_vy \- 64, \_vw \+ 128, \_vh \+ 128, false);

The above code deactivates all instances except the one that is running the code and then activates a region within the room.
