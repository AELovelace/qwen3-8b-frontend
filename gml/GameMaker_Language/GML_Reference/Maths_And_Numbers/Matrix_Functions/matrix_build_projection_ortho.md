# matrix\_build\_projection\_ortho

This function builds an orthographic projection matrix based on the specified parameters listed below (this is the default projection method used when you create a room in GameMaker without changing anything). It can optionally write the result to an existing matrix that you specify.

Sometimes you need to switch from a perspective projection to an orthographic projection, which is what this function is for. It is typically used to draw an overlay, for example, to show the score or other aspects as this gives a "flat" view of the elements drawn (i.e.: no perspective) in a 3D game. See the image below to get an idea of the difference between orthographic and perspective views.

 
  You may also need to temporarily switch off hidden surface removal if you want the information to be drawn regardless of the current depth value.

#### Syntax:

matrix\_build\_projection\_ortho(width, height, znear, zfar, \[result\_matrix])

| Argument | Type | Description |
| --- | --- | --- |
| width | [Real](../../../GML_Overview/Data_Types.md) | The width of the projection. |
| height | [Real](../../../GML_Overview/Data_Types.md) | The height of the projection. |
| znear | [Real](../../../GML_Overview/Data_Types.md) | The distance to the near clipping plane. |
| zfar | [Real](../../../GML_Overview/Data_Types.md) | The distance to the far clipping plane. |
| result\_matrix | [Matrix](Matrix_Functions.md) | The existing matrix in which to store the result. |

 

#### Returns:

[Matrix](Matrix_Functions.md)

 

#### Example:

viewmat \= matrix\_build\_lookat(640, 240, \-10, 640, 240, 0, 0, 1, 0\);  

 projmat \= matrix\_build\_projection\_ortho(640, 480, 1\.0, 32000\.0\);  

 camera\_set\_view\_mat(view\_camera\[0], viewmat);  

 camera\_set\_proj\_mat(view\_camera\[0], projmat);

The above code creates a new look\-at matrix and orthographic projection matrix, stores their IDs in local variables and then uses them to set the view and projection matrices for the camera assigned to viewport\[0].
