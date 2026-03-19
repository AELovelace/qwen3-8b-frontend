# gpu\_get\_texrepeat\_ext

With this function you can check to see whether texture repeating is enabled (returns true) or not (returns false) for a given shader sampler texture.

 

#### Syntax:

gpu\_get\_texrepeat\_ext(sampler\_id)

| Argument | Type | Description |
| --- | --- | --- |
| sampler\_id | [Shader Sampler Handle](../../Asset_Management/Shaders/shader_get_sampler_index.md) | The sampler id from the shader. |

 

#### Returns:

[Boolean](../../../GML_Overview/Data_Types.md)

 

#### Example:

var s\_tex \= shader\_get\_sampler\_index(shader\_glass, "s\_NoiseSampler");  

 if (!gpu\_get\_texrepeat\_ext(s\_tex))  

 {  

     gpu\_set\_texrepeat\_ext(s\_tex, true);  

 }

The above code checks to see if texture filtering off for a specific sampler ID (stored in a local variable) and switches it on if it's not.
