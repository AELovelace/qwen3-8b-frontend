# shader\_get\_uniform

This function gets the handle of the shader constant with the given name.

Since you cannot change the value of a shader constant within the shader itself, you have to set it before calling the shader using one of the available **uniform set** functions. However, to be able to do that you must first call this function to get the "handle" of the shader constant that you want to change.

 Although a shader is made up of two discreet programs (vertex and fragment) this function will not differentiate between the two and will return the handle of the shader constant from either of them.

 

#### Syntax:

shader\_get\_uniform(shader, uniform)

| Argument | Type | Description |
| --- | --- | --- |
| shader | [Shader Asset](../../../../The_Asset_Editors/Shaders.md) | The shader to use |
| uniform | [String](../../../GML_Overview/Data_Types.md) | The shader constant to get the handle of |

 

#### Returns:

[Shader Uniform Handle](shader_get_uniform.md)

 

#### Example:

shader\_params \= shader\_get\_uniform(sh\_glass, "u\_RefractColour");

The above code will get the handle of the shader constant u\_RefractColour, used in the shader sh\_glass.
