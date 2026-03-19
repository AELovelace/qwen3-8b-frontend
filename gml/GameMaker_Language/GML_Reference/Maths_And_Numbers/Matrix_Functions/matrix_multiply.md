# matrix\_multiply

This function multiplies two matrices together to create a new matrix and returns the result as a new matrix, or optionally writes the result to an existing matrix that you specify.

The order of the matrices in the multiplication affects the result. This function multiplies the two matrices you pass it in the following order: 

result \= matrix2 \* matrix1;

To know the order in which the transforms held by these matrices are applied this needs to be read from right to left, i.e. the result matrix *first* applies the transform stored in matrix1 and *then* the transform stored in matrix2.

  You cannot use a matrix constant as an argument with this function, so if you wish to multiply the (for example) view matrix with a custom matrix that you have built, you must first call [matrix\_get](matrix_get.md) and assign the view matrix values to an array variable, then multiply it by your custom matrix, and then set the chosen matrix (view, projection or world).

 

#### Syntax:

matrix\_multiply(matrix1, matrix2, \[result\_matrix])

| Argument | Type | Description |
| --- | --- | --- |
| matrix1 | [Matrix](Matrix_Functions.md) | The first matrix to use (storing the first transformation to apply) |
| matrix2 | [Matrix](Matrix_Functions.md) | The second matrix to use (storing the second transformation to apply) |
| result\_matrix | [Matrix](Matrix_Functions.md) | An existing matrix in which to store the result. If this argument isn't specified, the function returns the result as a new matrix. |

 

#### Returns:

[Matrix](Matrix_Functions.md)

 

#### Example 1: Basic Use

var \_v\_matrix \= matrix\_get(matrix\_view);  

 var \_new\_matrix \= matrix\_multiply(\_v\_matrix, my\_matrix);  

 matrix\_set(matrix\_view, \_new\_matrix);

The above code gets the current view matrix, multiplies that with a custom matrix and sets the view matrix to the resulting matrix.

 

#### Example 2: Using an Existing Matrix to Store the Result

Create Event

mat\_result \= matrix\_build\_identity();  

  

 mat\_one \= matrix\_build(0, 0, 10, 0, 0, 90, 1, 1, 1\);  

 mat\_two \= matrix\_build(10, 0, 4, 30, 45, 0, 1, 1, 1\);
 

Step Event

mat\_one\[12] \= 100 \+ lengthdir\_x(100, current\_time/100\);  

 matrix\_multiply(mat\_one, mat\_two, mat\_result);

This code creates an identity matrix and two other matrices in the Create event to be used for a matrix multiplication. In the Step event, the matrix element at array index 12 is set to a new value and matrix\_multiply is called with the two matrices. The existing matrix mat\_result is used to store the result, which saves the need to create a new matrix on every call to the function.

 

#### Example 3: Drawing a Rectangle Relative to a Circle

Draw Event

var \_mat\_child\_local \= matrix\_build(100, 100, 0, 0, 0, current\_time/2, 1, 1, 1\);  

 var \_mat\_parent\_global \= matrix\_build(x, y, 0, 0, 0, current\_time/12 \+ dsin(current\_time/4\) \* 30, 1, 1, 1\);  

 var \_mat\_child\_global \= matrix\_multiply(\_mat\_child\_local, \_mat\_parent\_global);  

  

 matrix\_set(matrix\_world, \_mat\_parent\_global);  

 draw\_circle\_color(0, 0, 100, c\_blue, c\_blue, false);  

 matrix\_set(matrix\_world, \_mat\_child\_global);  

 draw\_rectangle\_color(\-10, \-10, 10, 10, c\_red, c\_red, c\_red, c\_red, false);  

 matrix\_set(matrix\_world, matrix\_build\_identity());
 

The code example above shows how matrix\_multiply can be used to draw a rectangle shape relative to a circle shape.

In the Draw event, two matrices are built using [matrix\_build](matrix_build.md) and stored in variables \_mat\_child\_local and \_mat\_parent\_global. The first matrix represents the transform of the rectangle relative to the circle, the second matrix that of the circle relative to the room. Using matrix\_multiply a third matrix is then created that is the product of the first two matrices. The rectangle's transform is the first argument passed to the function, the circle's transform the second, i.e. the transformation stored in the resulting matrix will *first* apply the rectangle's transform, *then* the circle's transform.

Next, the world matrix is set to \_mat\_parent\_global using [matrix\_set](matrix_set.md) and a blue circle with radius 100 is drawn. After that, the world matrix is set to \_mat\_child\_global and a red square with a side of 20 is drawn.

Finally, the world matrix is reset to an identity matrix to not affect further drawing.
