# matrix\_build\_lookat

This function builds a "look\-at" (view) matrix and returns it as a new matrix, or optionally writes the result to an existing matrix that you specify.

Since this function modifies the view matrix and not the projection matrix, you should first initialise the projection matrix using the other matrix function [matrix\_build\_projection\_perspective](matrix_build_projection_perspective.md), then use this function to move the view camera around within the projection.

To set the view you first need to define the position you look *from*, which is indicated by the parameters (xfrom, yfrom, zfrom). Next you must specify the direction you look *at* and this is done by giving a second point to look towards with the arguments (xto, yto, zto). Finally, you can still rotate the camera around the line from the viewpoint to the looking point, and to specify this we must give an "up" vector \- the direction that is upwards in the camera. This is given by the last three arguments (xup, yup, zup).

 

#### Syntax:

matrix\_build\_lookat(xfrom, yfrom, zfrom, xto, yto, zto, xup, yup, zup, \[result\_matrix])

| Argument | Type | Description |
| --- | --- | --- |
| xfrom | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate of the position to look from. |
| yfrom | [Real](../../../GML_Overview/Data_Types.md) | The y coordinate of the position to look from. |
| zfrom | [Real](../../../GML_Overview/Data_Types.md) | The z coordinate of the position to look from. |
| xto | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate of the position to look to. |
| yto | [Real](../../../GML_Overview/Data_Types.md) | The y coordinate of the position to look to. |
| zto | [Real](../../../GML_Overview/Data_Types.md) | The z coordinate of the position to look to. |
| xup | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate of the "up" vector. |
| yup | [Real](../../../GML_Overview/Data_Types.md) | The y coordinate of the "up" vector. |
| zup | [Real](../../../GML_Overview/Data_Types.md) | The z coordinate of the "up" vector. |
| result\_matrix | [Matrix](Matrix_Functions.md) | The existing matrix to write the result to. |

 

#### Returns:

[Matrix](Matrix_Functions.md)

 

#### Example:

viewmat \= matrix\_build\_lookat(640, 240, \-10, 640, 240, 0, 0, 1, 0\);  

 projmat \= matrix\_build\_projection\_ortho(640, 480, 1\.0, 32000\.0\);  

 camera\_set\_view\_mat(view\_camera\[0], viewmat);  

 camera\_set\_proj\_mat(view\_camera\[0], projmat);

The above code creates a new look\-at matrix and orthographic projection matrix, stores them in variables and then uses them to set the view and projection matrices for the camera assigned to viewport\[0].
