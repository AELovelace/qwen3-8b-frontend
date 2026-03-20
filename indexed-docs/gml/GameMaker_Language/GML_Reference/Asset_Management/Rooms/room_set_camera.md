# room\_set\_camera

This function assigns a camera to a specific viewport in a room other than the current one.

You supply the room, the view index (from 0 to 7\) and then the index of the camera to use.

 

#### Syntax:

room\_set\_camera(rm, vind, camera)

| Argument | Type | Description |
| --- | --- | --- |
| rm | [Room Asset](../../../../The_Asset_Editors/Rooms.md) | The room to set the view camera of |
| vind | [Real](../../../GML_Overview/Data_Types.md) | The index of the viewport to assign the camera to |
| camera | [Camera ID](../../Cameras_And_Display/Cameras_And_Viewports/camera_create.md) | The index of the camera to assign |

 

#### Returns:

N/A

 

#### Example:

global.myroom \= room\_add();  

 room\_set\_camera(global.myroom, 0, global.MainCam);

The above code assigns a camera in a newly created room to viewport \[0].
