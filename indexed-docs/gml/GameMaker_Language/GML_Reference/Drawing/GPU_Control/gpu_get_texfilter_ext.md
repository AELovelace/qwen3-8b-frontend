# gpu\_get\_texfilter\_ext

With this function you can check to see whether texture interpolation (linear interpolation) is enabled (returns true) or not (returns false) for a given shader sampler texture.

**NOTE**: On the HTML5 target, this function will only work with WebGL enabled.

 

#### Syntax:

gpu\_get\_texfilter\_ext(sampler\_id)

| Argument | Type | Description |
| --- | --- | --- |
| sampler\_id | [Shader Sampler Handle](../../../../../GameMaker_Language/GML_Reference/Asset_Management/Shaders/shader_get_sampler_index.md) | The sampler id from the shader. |

 

#### Returns:

[Boolean](../../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

var s\_tex \= shader\_get\_sampler\_index(shader\_glass, "s\_NoiseSampler");  

 if (gpu\_get\_texfilter\_ext(s\_tex))   

 {  

     gpu\_set\_texfilter\_ext(s\_tex, false);  

 }  

 else  

 {  

     gpu\_set\_texfilter\_ext(s\_tex, true);  

 }

The above code checks to see if texture filtering is on or off for a specific sampler ID (stored in a local variable) and switches it accordingly.
