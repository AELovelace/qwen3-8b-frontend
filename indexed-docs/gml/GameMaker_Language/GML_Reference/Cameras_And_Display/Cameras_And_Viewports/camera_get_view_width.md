# camera\_get\_view\_width

This function can be used to retrieve the width (in pixels) of the given camera view.

 
 

#### Syntax:

camera\_get\_view\_width(camera\_id)

| Argument | Type | Description |
| --- | --- | --- |
| camera\_id | [Camera ID](camera_create.md) | The unique camera ID value returned when you created the camera |

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

var \_vw \= camera\_get\_view\_width(view\_camera\[0]) / 2;  

 var \_vh \= camera\_get\_view\_height(view\_camera\[0]) / 2;  

 camera\_set\_view\_pos(view\_camera\[0], x \- \_vw, y \- \_vh);

The above code retrieves the width and height of the camera assigned to viewport\[0] and then sets its position relative to the center.
