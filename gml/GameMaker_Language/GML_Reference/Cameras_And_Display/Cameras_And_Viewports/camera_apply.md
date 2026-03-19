# camera\_apply

This function immediately applies the given camera's settings to the current camera view being rendered and sets it as the active camera.

While you can change any view camera's settings using the specific camera\_set\_\* functions, the new settings will not be used for rendering until the *next* game frame, but with this function you can make those changes immediately. If you are using multiple views, the function should be used in the **Draw** event and you can use the variable [view\_current](view_current.md) to selectively apply the given camera only to the camera view currently being rendered.

  If you call this function at a point in the draw cycle where the [default camera](camera_get_default.md "camera_get_default()") (i.e.: the internal camera GameMaker uses when no view cameras are active) is the active camera, the changes will be overwritten the next game frame by the internal settings for drawing the room.

 

#### Syntax:

camera\_apply(camera\_id)

| Argument | Type | Description |
| --- | --- | --- |
| camera\_id | [Camera ID](camera_create.md) | The unique camera ID value returned when you created the camera |

 

#### Returns:

N/A

 

#### Example:

Draw Event

if (view\_current \=\= 0\)  

 {  

     camera\_apply(cutscene\_cam);  

 }

The above code (in a Draw event) checks to see which camera view is currently being rendered. If it is camera view\[0], the settings for the camera referenced by the variable cutscene\_cam are applied to it.
