# matrix\_build\_projection\_perspective

This function builds a perspective projection matrix based on the dimensions of the near clipping plane, using the specified parameters listed below, and optionally writes the result to a matrix that you specify.

Note that the field of view of the camera will vary depending on the width, height and znear values specified, as the projection width and height are placed at the Z position specified in the znear argument.

For example, given a constant size of 640x480, the field of view will be wider if znear is closer to the camera, but it will be narrower if znear is far away from the camera. This behaviour is demonstrated in the following visual:

Due to this, it is recommended to use a znear value that is identical to the width of the projection, resulting in the field of view being consistent with an equivalent orthographic projection.

 
 

#### Syntax:

matrix\_build\_projection\_perspective(width, height, znear, zfar, \[result\_matrix])

| Argument | Type | Description |
| --- | --- | --- |
| width | [Real](../../../GML_Overview/Data_Types.md) | The width of the projection at the near Z position. |
| height | [Real](../../../GML_Overview/Data_Types.md) | The height of the projection at the near Z position. |
| znear | [Real](../../../GML_Overview/Data_Types.md) | The near clipping plane. |
| zfar | [Real](../../../GML_Overview/Data_Types.md) | The far clipping plane. |
| result\_matrix | [Matrix](Matrix_Functions.md) | The existing matrix to write the result to. |

 

#### Returns:

[Matrix](Matrix_Functions.md)

 

#### Example:

var \_projmat \= matrix\_build\_projection\_perspective(640, 480, 640\.0, 32000\.0\);  

 camera\_set\_proj\_mat(view\_camera\[0], \_projmat);

The above code creates a perspective projection and then uses the matrix returned to set the camera assigned to viewport\[0].
