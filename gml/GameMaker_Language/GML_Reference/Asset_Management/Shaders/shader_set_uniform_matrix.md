# shader\_set\_uniform\_matrix

This function sets the value (or values) of a shader constant to the current transform matrix (as set using the [Matrix Functions](../../Maths_And_Numbers/Matrix_Functions/Matrix_Functions.md)).

You must previously have gotten the "handle" of the constant using the function [shader\_get\_uniform](shader_get_uniform.md).

 
 

#### Syntax:

shader\_set\_uniform\_matrix(handle)

| Argument | Type | Description |
| --- | --- | --- |
| handle | [Shader Uniform Handle](shader_get_uniform.md) | The handle of the shader constant to set. |

 

#### Returns:

N/A

 

#### Example:

shader\_set(sh\_glass);  

 shader\_matrix \= shader\_get\_uniform(sh\_glass, "u\_vMatrix");  

 shader\_set\_uniform\_matrix(shader\_matrix);  

 draw\_self();  

 shader\_reset();

The above code will get the handle of the shader constant u\_vMatrix then set that constant to the current transform matrix.
