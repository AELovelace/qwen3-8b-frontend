# matrix\_get

This function returns the currently used matrix of the given type (which can be either the world, view or projection matrix) as a new matrix, or optionally writes the result to an existing matrix that you specify.

The matrix is returned as an [array](../../../GML_Overview/Arrays.md) of 16 elements, corresponding to the given 4x4 matrix type, where column 1 is stored in elements \[0 \- 3], column 2 is stored in elements \[4 \-7], etc. (see the images on the [main page](Matrix_Functions.md)).

The available matrices are *view*, *projection* and *world*, for which you would use one of the following constants:

| [Matrix Type Constant](matrix_get.md) | |
| --- | --- |
| Constant | Description |
| matrix\_view | The current view matrix |
| matrix\_projection | The current projection matrix |
| matrix\_world | The current world matrix |

 

#### Syntax:

matrix\_get(type, \[result\_matrix])

| Argument | Type | Description |
| --- | --- | --- |
| type | [Matrix Type Constant](matrix_get.md) | The type of matrix to get (see the *constants* listed above) |
| result\_matrix | [Matrix](Matrix_Functions.md) | The existing matrix to write the result to |

 

#### Returns:

[Matrix](Matrix_Functions.md)

 

#### Example:

v\_array \= matrix\_get(matrix\_view);

The above code will get the values of the current view matrix and store them in a variable v\_array.
