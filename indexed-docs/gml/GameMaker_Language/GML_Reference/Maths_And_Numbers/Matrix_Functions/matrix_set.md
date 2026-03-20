# matrix\_set

This function sets the current matrix of the given type (world, view or projection) to the given matrix.

The available matrix types are *world*, *view*, and *projection*, which are represented by the following constants:

Matrix Type Constant
| Constant | Description |
| --- | --- |
| matrix\_world | The current world matrix |
| matrix\_view | The current view matrix |
| matrix\_projection | The current projection matrix |

You can create a matrix using the [matrix\_build\*](Matrix_Functions.md#func_ref_building_matrices "Building Matrices") functions or simply build the array yourself and pass that into the function.

 
 

#### Syntax:

matrix\_set(type, matrix)

| Argument | Type | Description |
| --- | --- | --- |
| type | [Matrix Type Constant](matrix_get.md) | The type of matrix to get the values of (see the *constants* listed above) |
| matrix | [Matrix](Matrix_Functions.md) | The matrix data as an array |

 

#### Returns:

N/A

 

#### Example:

Draw Event

var \_world\_matrix \= matrix\_build(x, y, 0, 0, 0, image\_angle, 1, 1, 1\);  

matrix\_set(matrix\_world, \_world\_matrix);  

 draw\_sprite(sprite\_index, 0, 0, 0\);  

 matrix\_set(matrix\_world, matrix\_build\_identity());
 

The above code draws an instance's sprite at its position by changing the world matrix.

First, a world matrix is created with [matrix\_build](matrix_build.md) which first does a rotation about [image\_angle](../../Asset_Management/Sprites/Sprite_Instance_Variables/image_angle.md) degrees and then moves to the position given by [x](../../Asset_Management/Instances/Instance_Variables/x.md) and [y](../../Asset_Management/Instances/Instance_Variables/y.md). Next, the world matrix is set to this matrix in a call to matrix\_set and the [sprite\_index](../../Asset_Management/Sprites/Sprite_Instance_Variables/sprite_index.md) of the instance executing the Draw event is drawn with [draw\_sprite](../../Drawing/Sprites_And_Tiles/draw_sprite.md) (note that the x and y passed to this function must be 0, since it is the world matrix that moves the sprite to the instance's (x, y) position!). Finally, the world matrix is reset to an identity matrix in another call to matrix\_set.
