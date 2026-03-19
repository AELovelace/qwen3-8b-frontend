# matrix\_build\_projection\_perspective\_fov

This function builds a perspective projection matrix based on field of view, using the specified parameters listed below, and optionally writes the result to a matrix that you specify.

 
 

#### Syntax:

matrix\_build\_projection\_perspective\_fov(fov\_y, aspect, znear, zfar, \[result\_matrix])

| Argument | Type | Description |
| --- | --- | --- |
| fov\_y | [Real](../../../GML_Overview/Data_Types.md) | The vertical angle of the field of view. |
| aspect | [Real](../../../GML_Overview/Data_Types.md) | The aspect ratio of the field of view. |
| znear | [Real](../../../GML_Overview/Data_Types.md) | The distance to the near clipping plane. |
| zfar | [Real](../../../GML_Overview/Data_Types.md) | The distance to the far clipping plane. |
| result\_matrix | [Matrix](Matrix_Functions.md) | The existing matrix to write the result to. |

 

#### Returns:

[Matrix](Matrix_Functions.md)

 

#### Example:

var \_projmat \= matrix\_build\_projection\_perspective\_fov(60, 320/240, 1\.0, 32000\.0\);  

 camera\_set\_proj\_mat(view\_camera\[0], \_projmat);

The above code creates a field of view projection matrix which is then stored in a variable. This matrix is then used to set up the camera assigned to viewport\[0].
