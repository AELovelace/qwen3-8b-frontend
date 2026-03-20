# matrix\_inverse

This function returns a new matrix that is the inverse of the matrix that you pass it, or optionally writes the result to an existing matrix that you specify.

The inverse of a matrix is the matrix that, when multiplied with the original matrix, is equal to an identity matrix.

From a more practical perspective, the inverse of a matrix *undoes* the transformation of the original matrix. For example, the matrix matrix\_build(100, 100, 0, 90, 0, 0, 1, 1, 1\) first rotates about x by 90 degrees and then moves right 100 and down 100\. Its inverse matrix matrix\_inverse(matrix\_build(100, 100, 0, 90, 0, 0, 1, 1, 1\)) first moves left 100 and up 100 and then rotates about x by \-90 degrees, performing the exact same steps in reverse order. The product of these matrices (i.e. matrix\_multiply(inverse, transform)) will be an identity matrix.

 

#### Syntax:

matrix\_inverse(matrix, \[result\_matrix])

| Argument | Type | Description |
| --- | --- | --- |
| matrix | [Matrix](Matrix_Functions.md) | The matrix to get the inverse of |
| result\_matrix | [Matrix](Matrix_Functions.md) | The existing matrix to write the result to |

 

#### Returns:

[Matrix](Matrix_Functions.md) (or [undefined](../../../GML_Overview/Data_Types.md) in case a new matrix is returned and the matrix doesn't have an inverse)

 

#### Example:

transform \= matrix\_build(x, y, 0, 90, 0, direction, 1, 1, 1\);  

 transform\_inverse \= matrix\_inverse(transform);  

  

 transform\_product \= matrix\_multiply(transform, transform\_inverse);  

  

 show\_debug\_message(transform);  

 show\_debug\_message(transform\_inverse);  

 show\_debug\_message(transform\_product);
 

The above code shows how to build a transform matrix, get its inverse using matrix\_inverse and multiply the two matrices back together. The three matrices, i.e. the original matrix, its inverse and their product are then output in a debug message. Note that the product of the matrices is equal to an identity matrix (i.e. [matrix\_build\_identity](matrix_build_identity.md)).
