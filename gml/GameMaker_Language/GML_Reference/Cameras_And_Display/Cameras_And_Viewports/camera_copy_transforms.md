# camera\_copy\_transforms

This function copies all transform\-related settings of the source camera to the destination camera.

More specifically, it copies the source camera's view and projection matrices, as well as the view position, size, speed, border and angle values.

  This function is mostly meant for internal use by GameMaker when working with filters and effects though you can use it as a convenient way to copy one camera's transforms to another one.

  The function *doesn't* copy the source camera's *begin, end and update scripts*.

 

#### Syntax:

camera\_copy\_transforms(dest\_camera, src\_camera)

| Argument | Type | Description |
| --- | --- | --- |
| dest\_camera | [Camera ID](../../../../../GameMaker_Language/GML_Reference/Cameras_And_Display/Cameras_And_Viewports/camera_create.md) | The camera to copy the source camera's transforms to (projection and view matrix) |
| src\_camera | [Camera ID](../../../../../GameMaker_Language/GML_Reference/Cameras_And_Display/Cameras_And_Viewports/camera_create.md) | The camera that contains the projection and view matrices that you want to copy |

 

#### Returns:

N/A

 

#### Example:

cam1 \= view\_camera\[0];  

 cam2 \= camera\_create();  

camera\_copy\_transforms(cam2, cam1\);
 

The above code assigns the camera that GameMaker creates internally for view 0 (that you can first configure in [The Room Editor](../../../../The_Asset_Editors/Rooms.md)) to an instance variable cam1. Then it creates a new, "empty" camera cam2 using the function [camera\_create](camera_create.md). It then copies cam1's transform\-related settings to cam2 by calling camera\_copy\_transforms.
