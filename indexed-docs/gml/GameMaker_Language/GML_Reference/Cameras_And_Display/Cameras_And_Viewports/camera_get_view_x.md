# camera\_get\_view\_x

This function can be used to retrieve the x position of the view for a given camera.

 

 
 

#### Syntax:

camera\_get\_view\_x(camera\_id)

| Argument | Type | Description |
| --- | --- | --- |
| camera\_id | [Camera ID](camera_create.md) | The unique camera ID value returned when you created the camera |

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

var \_vx \= camera\_get\_view\_x(view\_camera\[0]);  

 var \_vy \= camera\_get\_view\_y(view\_camera\[0]);  

 draw\_text(\_vx \+ 5, \_vy \+ 5, "SCORE: " \+ string(score));

The above code retrieves the position of the camera assigned to viewport\[0] and then draws text relative to that position.
