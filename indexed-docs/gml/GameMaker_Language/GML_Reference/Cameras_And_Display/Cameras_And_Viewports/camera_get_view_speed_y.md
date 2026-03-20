# camera\_get\_view\_speed\_y

This function can be used to retrieve the movement speed of the given camera along the y axis (vertical movement), which can be set in the room properties (see [Cameras And Viewports](../../../../The_Asset_Editors/Room_Properties/Room_Properties.md#h)) or via the function [camera\_set\_view\_speed](camera_set_view_speed.md)). The return value will be in pixels per game frame.

 

#### Syntax:

camera\_get\_view\_speed\_y(camera\_id)

| Argument | Type | Description |
| --- | --- | --- |
| camera\_id | [Camera ID](camera_create.md) | The unique camera ID value returned when you created the camera |

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

var \_xs \= camera\_get\_view\_speed\_x(view\_camera\[0]);  

 var \_ys \= camera\_get\_view\_speed\_y(view\_camera\[0]);  

 if (\_xs !\= 5 \|\| \_ys !\= 5\)  

 {  

     camera\_set\_view\_speed(view\_camera\[0], 5, 5\);  

 }

The above code retrieves the xspeed and yspeed of the camera assigned to viewport\[0] and then checks this to see if it matches the given value. If it does not then the view camera is set to that speed.
