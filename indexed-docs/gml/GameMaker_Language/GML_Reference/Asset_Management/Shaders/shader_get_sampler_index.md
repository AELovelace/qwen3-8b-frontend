# shader\_get\_sampler\_index

This function gets the handle of the shader sampler with the given name.

Since you cannot change the value of a shader sampler within the shader itself, you have to set it before calling the shader using the function [texture\_set\_stage](../../Drawing/Textures/texture_set_stage.md). However, to be able to do that you must first call this function to get the "handle" of the shader sampler that you want to set.

  Although a shader is made up of two discreet programs (vertex and fragment), this function will not differentiate between the two and will return the handle of the shader sampler from either of them.

 

#### Syntax:

shader\_get\_sampler\_index(shader, uniform)

| Argument | Type | Description |
| --- | --- | --- |
| shader | [Shader Asset](../../../../The_Asset_Editors/Shaders.md) | The shader to use |
| uniform | [String](../../../GML_Overview/Data_Types.md) | The shader sampler to get the handle of |

 

#### Returns:

[Shader Sampler Handle](shader_get_sampler_index.md)

 

#### Example:

var \_sampler \= shader\_get\_sampler\_index(sh\_glass, "u\_BackgroundSampler");  

 var \_texture \= sprite\_get\_texture(sprite\_index, 0\);  

 shader\_set(sh\_glass);  

 texture\_set\_stage(\_sampler, \_texture);  

  

 // Draw something here  

  

 shader\_reset();
 

The above code gets the *handle* for a sampler uniform u\_BackgroundSampler  defined in a shader  sh\_glass. It then sets that shader constant to the given texture.
