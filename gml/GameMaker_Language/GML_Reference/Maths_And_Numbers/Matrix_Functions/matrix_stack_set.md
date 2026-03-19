# matrix\_stack\_set

This function overwrites the current top of the matrix stack with the specified matrix.

 

#### Syntax:

matrix\_stack\_set(matrix)

| Argument | Type | Description |
| --- | --- | --- |
| matrix | [Matrix](Matrix_Functions.md) | The matrix index to use |

 

#### Returns:

N/A

 

#### Example:

var \_matrix \= matrix\_build(x, y, 0, 0, 0, 0, 1, 1, 1\);  

 matrix\_stack\_set(\_matrix);

The above code builds a new matrix and stores the resulting matrix index in a temporary variable \_matrix before replacing the top of the matrix stack with it.
