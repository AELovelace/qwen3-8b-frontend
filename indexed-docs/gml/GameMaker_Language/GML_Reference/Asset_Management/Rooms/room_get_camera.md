# room\_get\_camera

This function gets the unique index ID of the camera assigned to a specific view in a room other than the current one.

You give the room to use, the viewport to use (from 0 to 7\) and the function will return a camera index.

 

#### Syntax:

room\_get\_camera(rm, vind)

| Argument | Type | Description |
| --- | --- | --- |
| rm | [Room Asset](../../../../The_Asset_Editors/Rooms.md) | The room to get the view camera of |
| vind | [Real](../../../GML_Overview/Data_Types.md) | The index of the viewport to get the camera of |

 

#### Returns:

[Camera ID](../../Cameras_And_Display/Cameras_And_Viewports/camera_create.md)

 

#### Example:

var \_cam \= room\_get\_camera(rm\_game, 0\);  

 if (\_cam !\= global.main\_cam)  

 {  

     room\_set\_camera(rm\_game, 0, global.main\_cam);  

 }

The above code assigns a camera in a newly created room to viewport 0\.
