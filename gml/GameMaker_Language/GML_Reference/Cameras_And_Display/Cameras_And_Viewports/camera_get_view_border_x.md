# camera\_get\_view\_border\_x

This function can be used to retrieve the x (horizontal) border value set for the given camera, which can be set in the room properties (see [Cameras And Viewports](../../../../The_Asset_Editors/Room_Properties/Room_Properties.md#h)) or via the function [camera\_set\_view\_border](camera_set_view_border.md)). The return value will be in pixels.

 

#### Syntax:

camera\_get\_view\_border\_x(camera\_id)

| Argument | Type | Description |
| --- | --- | --- |
| camera\_id | [Camera ID](camera_create.md) | The unique camera ID value returned when you created the camera |

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

var \_xb \= camera\_get\_view\_border\_x(view\_camera\[0]);  

 var \_yb \= camera\_get\_view\_border\_y(view\_camera\[0]);  

 if (\_xb !\= 200 \|\| \_yb !\= 200\)  

 {  

     camera\_set\_view\_border(view\_camera\[0], 200, 200\);  

 }

The above code retrieves the xborder and yborder values of the camera assigned to viewport\[0] and then checks this to see if it matches the given value. If it does not then the view camera is set to the given value.
