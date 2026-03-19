# view\_set\_camera

This function assigns the given camera to the given viewport.

You give the viewport to set (from 0 to 7\), and supply the unique camera (as returned by the [camera\_create](camera_create.md) functions or when you use [view\_get\_camera](view_get_camera.md)). If you give a value of \-1 as the camera ID then you are removing a camera from the viewport and note that if that viewport is enabled and visible you may get some unpredictable results.

 

#### Syntax:

view\_set\_camera(viewport, camera\_id)

| Argument | Type | Description |
| --- | --- | --- |
| viewport | [Real](../../../GML_Overview/Data_Types.md) | The viewport to target (0 \- 7\) |
| camera\_id | [Camera ID](camera_create.md) | The unique camera value returned when you created the camera |

 

#### Returns:

N/A

 

#### Example:

var \_cam \= camera\_create\_view(0, 0, 640, 480, 0, obj\_player, 5, 5, \-1, \-1\);  

 view\_set\_camera(0, \_cam);

The above code will create a new camera and then assign it viewport\[0].
