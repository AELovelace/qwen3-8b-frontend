# gpu\_set\_tex\_mip\_filter\_ext

With this function you can set the mip filter mode for a given shader sampler. You supply the handle for the shader sampler (as returned by the function [shader\_get\_sampler\_index()](../../Asset_Management/Shaders/shader_get_sampler_index.md), and then one of the mode value constants listed below.

 

| Constant | Description |
| --- | --- |
| tf\_point | This means that blending between mipmap levels is disabled, which can cause visible texture transitions, but gives the best performance. |
| tf\_linear | This means that blending between mipmap levels is enabled (this is also known as *trilinear filtering*), which smooths the texture transitions, but it will give a minor hit to performance. |
| tf\_anisotropic | This means that anisotropic filtering is enabled, which greatly improves texture transition quality and can reduce the blurring visible with other filtering modes, but it has the highest hit on performance. |

 

#### Syntax:

gpu\_set\_tex\_mip\_filter\_ext(sampler\_index, filter)

 

| Argument | Type | Description |
| --- | --- | --- |
| sampler\_index | [Shader Sampler Handle](../../Asset_Management/Shaders/shader_get_sampler_index.md) | The shader sampler to get. |
| filter | [Mipmapping Filter Constant](gpu_set_tex_mip_filter.md) | The mip filter mode to use (a constant, default: tf\_point). |

 

#### Returns:

N/A

 

#### Example:

var \_sampleIndex \= shader\_get\_sampler\_index(shd\_Glass, "s\_Background");  

 var \_spriteTex \= sprite\_get\_texture(sprite\_index, 0\);  

 shader\_set(shd\_Glass);  

 if (gpu\_get\_tex\_mip\_filter\_ext(\_sampleIndex) !\= tf\_point)  

 {  

     gpu\_set\_tex\_mip\_filter\_ext(\_sampleIndex, tf\_point);  

 }  

 texture\_set\_stage(\_sampleIndex, \_spriteTex);  

 shader\_reset();

The above code sets the mip filter mode to tf\_point (disabling mipmapping) for the given shader texture sampler if it has not already been set.
