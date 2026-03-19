# shader\_set

With this function you can set the drawing target to the given shader and all further drawing will be done using that. You can end shader use with the function [shader\_reset()](shader_reset.md).

 

#### Syntax:

shader\_set(shader)

| Argument | Type | Description |
| --- | --- | --- |
| shader |  | The handle of the shader to use. |

 

#### Returns:

 

#### Example:

shader\_set(shader\_Glass);
   

 draw\_self();
   

 shader\_reset();

The above code will set a shader to be used for drawing, then draw the current sprite used for the instance using it.
