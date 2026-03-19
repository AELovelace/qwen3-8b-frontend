# camera\_get\_view\_target

This function can be used to retrieve the follow target of the given camera, which can be set in the room properties (see [Cameras And Viewports](../../../../The_Asset_Editors/Room_Properties/Room_Properties.md#h)) or with [camera\_set\_view\_target](camera_set_view_target.md). The return value can be an [Object Asset](../../../../The_Asset_Editors/Objects.md), an [Object Instance](../../Asset_Management/Instances/Instance_Variables/id.md) or \-1 if no follow target has been set.

 

#### Syntax:

camera\_get\_view\_target(camera\_id)

| Argument | Type | Description |
| --- | --- | --- |
| camera\_id | [Camera ID](camera_create.md) | The unique camera ID value returned when you created the camera |

 

#### Returns:

[Object Asset](../../../../The_Asset_Editors/Objects.md), [Object Instance](../../Asset_Management/Instances/Instance_Variables/id.md) or \-1

 

#### Example:

var \_target \= camera\_get\_view\_target(view\_camera\[0]);  

 if (\_target !\= obj\_player)  

 {  

     camera\_set\_view\_target(view\_camera\[0], obj\_player);  

 }

The above code retrieves the follow target of the camera assigned to viewport\[0] and then checks this to see if it matches the object index obj\_player. If it does not then the view camera is set to follow an instance of that object.
