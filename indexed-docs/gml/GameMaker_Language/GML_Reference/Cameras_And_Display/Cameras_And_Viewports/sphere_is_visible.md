# sphere\_is\_visible

This function returns if the sphere at the (x, y, z) position with the given radius is visible in the current view frustum.

The view frustum is defined by the currently set view and projection matrices, which are normally the [active](camera_get_active.md "camera_get_active()") camera's view and projection matrices. If you call this function after calling [camera\_apply](camera_apply.md), that camera's matrices are used instead.

 
 

#### Syntax:

sphere\_is\_visible(x, y, z, radius)

| Argument | Type | Description |
| --- | --- | --- |
| x | [Real](../../../GML_Overview/Data_Types.md) | The x component of the sphere's position |
| y | [Real](../../../GML_Overview/Data_Types.md) | The y component of the sphere's position |
| z | [Real](../../../GML_Overview/Data_Types.md) | The z component of the sphere's position |
| radius | [Real](../../../GML_Overview/Data_Types.md) | The sphere's radius |

 

#### Returns:

[Boolean](../../../GML_Overview/Data_Types.md)

 

#### Example:

Draw Event

var \_visible \= sphere\_is\_visible(x, y, z, radius);  

 if (!\_visible) { exit; }  

  

 vertex\_submit(my\_complex\_model, pr\_trianglelist, texture);
 

The above code calls sphere\_is\_visible in the Draw event to check if the bounding sphere surrounding the calling instance's 3D model is inside the current view frustum. If the result of this check is false, the sphere as well as the model it surrounds aren't visible on screen and there is no need to draw the 3D model, so the Draw event is exited. If the result of the check is true, the sphere and the 3D model are visible and the model is submitted to the GPU for drawing with a call to [vertex\_submit](../../Drawing/Primitives/vertex_submit.md).
