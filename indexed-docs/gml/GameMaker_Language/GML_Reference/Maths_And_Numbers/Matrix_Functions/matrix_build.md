# matrix\_build

This function creates a custom transformation matrix from 3\-dimensional (x, y, z) translation, rotation and scale values and returns it, or optionally writes the result to an existing matrix that you specify.

 
  When you set this matrix in a shader using [shader\_set\_uniform\_f\_array](../../Asset_Management/Shaders/shader_set_uniform_f_array.md), [shader\_set\_uniform\_matrix](../../Asset_Management/Shaders/shader_set_uniform_matrix.md) or [shader\_set\_uniform\_matrix\_array](../../Asset_Management/Shaders/shader_set_uniform_matrix_array.md), depending on the shader type and the target platform, you may receive the matrix transposed in the shader.

  When you build a matrix in this way, the order of operation is YXZ.

  Matrices returned by this function first apply rotation, then scale.

 

#### Syntax:

matrix\_build(x, y, z, xrotation, yrotation, zrotation, xscale, yscale, zscale, \[result\_matrix])

| Argument | Type | Description |
| --- | --- | --- |
| x | [Real](../../../GML_Overview/Data_Types.md) | The x component of the translation vector. |
| y | [Real](../../../GML_Overview/Data_Types.md) | The y component of the translation vector. |
| z | [Real](../../../GML_Overview/Data_Types.md) | The z component of the translation vector. |
| xrotation | [Real](../../../GML_Overview/Data_Types.md) | The angle to rotate around the x\-axis (in degrees). |
| yrotation | [Real](../../../GML_Overview/Data_Types.md) | The angle to rotate around the y\-axis (in degrees). |
| zrotation | [Real](../../../GML_Overview/Data_Types.md) | The angle to rotate around the z\-axis (in degrees). |
| xscale | [Real](../../../GML_Overview/Data_Types.md) | The x scale amount. |
| yscale | [Real](../../../GML_Overview/Data_Types.md) | The y scale amount. |
| zscale | [Real](../../../GML_Overview/Data_Types.md) | The z scale amount. |
| result\_matrix | [Matrix](Matrix_Functions.md) | The existing matrix to write the result to. |

 

#### Returns:

[Matrix](Matrix_Functions.md)

 

#### Example 1: Basic Use

t\_matrix \= matrix\_build(x, y, 0, 0, 90, 0, 1, 2, 1\);

The above code builds a new transformation matrix and stores it in a variable t\_matrix.

 

#### Example 2: Existing Matrix

Create Event

mat\_world \= matrix\_build\_identity();

Step Event

matrix\_build(x, y, 0, 0, 0, direction, 1, 1, 1, mat\_world);

The above code shows how an existing matrix can be reused.

In the Create event, an identity matrix is built using [matrix\_build\_identity](matrix_build_identity.md) and the result is assigned to a variable of the calling instance.

In the Step event, matrix\_build is called to create a matrix that rotates by [direction](../../Asset_Management/Instances/Instance_Variables/direction.md) degrees, then translates to the instance's ([x](../../Asset_Management/Instances/Instance_Variables/x.md), [y](../../Asset_Management/Instances/Instance_Variables/y.md)) position. Contrary to the first example, the return value isn't assigned to a variable here. Instead, the result is written to the matrix created before in the Create event, which is passed as the optional argument.
