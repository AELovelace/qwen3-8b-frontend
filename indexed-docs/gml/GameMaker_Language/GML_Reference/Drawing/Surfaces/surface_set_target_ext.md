# surface\_set\_target\_ext

This function is for use with the [Shader Functions](../../Asset_Management/Shaders/Shaders.md) and sets the MRT (0 \- 3\) for native level shaders (OpenGL ES, OpenGL, DX9, DX11\).

If you use this function to set render target index 0, the function sets the [default camera](../../Cameras_And_Display/Cameras_And_Viewports/camera_get_default.md "camera_get_default()") as the [active](../../Cameras_And_Display/Cameras_And_Viewports/camera_get_active.md "camera_get_active()") camera.

  MRT's are not supported on HTML5\.

 

#### Syntax:

surface\_set\_target\_ext(index, surface\_id)

| Argument | Type | Description |
| --- | --- | --- |
| index | [Real](../../../GML_Overview/Data_Types.md) | The render target index to use (from 0 to 3\). |
| surface\_id | [Surface](surface_create.md) | The surface to use. |

 

#### Returns:

[Boolean](../../../GML_Overview/Data_Types.md) Whether the render target was set successfully

 

#### Example:

surface\_set\_target\_ext(0, surf);

The above code sets the render target 0 to the surface stored in the variable surf.
