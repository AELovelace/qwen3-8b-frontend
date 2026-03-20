# instance\_activate\_all

With this function you can tell GameMaker to activate all instances that have been previously deactivated in a room. Note that activation is not instantaneous, and an instance that has been activated in this way will not be considered to be active until the end of the event in which the function was called.

 
 

#### Syntax:

instance\_activate\_all(\[collision\_space])

| Argument | Type | Description |
| --- | --- | --- |
| collision\_space | [Collision Space](instance_activate_all.md) | The collision space where instances will be activated |

 

#### Returns:

N/A

 

#### Example:

instance\_activate\_all();  

 var \_vx \= camera\_get\_view\_x(view\_camera\[0]);  

 var \_vy \= camera\_get\_view\_y(view\_camera\[0]);  

 var \_vw \= camera\_get\_view\_width(view\_camera\[0]);  

 var \_vh \= camera\_get\_view\_height(view\_camera\[0]);  

 instance\_deactivate\_region(\_vx \- 64, \_vy \- 64, \_vw \+ 128, \_vh \+ 128, false, false);

The above code activates all instances within the room and then deactivates those that are 64px outside of the limits of the current camera view.
