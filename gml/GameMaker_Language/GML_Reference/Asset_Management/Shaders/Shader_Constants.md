# Built\-In Shader Constants

Apart from the shader functions and constants defined in the OpenGL ES Shading Language (GLSL ES) [Reference Pages](https://registry.khronos.org/OpenGL/specs/es/2.0/GLSL_ES_Specification_1.00.pdf), there are also a number of built\-in shader constants available to you that are unique to GameMaker.

The names listed in the tables below refer to either:

- \#defines, which are similar to [Macros](../../../GML_Overview/Variables/Constants.md#h) in GML Code and are written in UPPERCASE
- Uniforms, which start with the gm\_ prefix

## Constants

The following constants (i.e. *defines*) can be used as array indices when using the shader array uniform gm\_Matrices:

Matrix Index Constant
| Constant | Description |
| --- | --- |
| MATRIX\_VIEW | This array index constant holds the index to the current view matrix. The index returned would be used as an array value when accessing the built\-in gm\_Matrices uniform within the shader code. |
| MATRIX\_PROJECTION | This array index constant holds the index to the current projection matrix. The index returned would be used as an array value when accessing the built\-in gm\_Matrices uniform within the shader code. |
| MATRIX\_WORLD | This array index constant holds the index to the current world matrix. This can be used for things like lighting if you have light information in world space. The index returned would be used as an array value when accessing the built\-in gm\_Matrices uniform within the shader code. |
| MATRIX\_WORLD\_VIEW | This array index constant holds the index to the result of the world and view matrices multiplied together. This is often used for things like fog. The index returned would be used as an array value when accessing the built\-in gm\_Matrices uniform within the shader code. |
| MATRIX\_WORLD\_VIEW\_PROJECTION | This array index constant holds the index to the result of the world, view and projection matrices multiplied together. This is the normal transformation matrix used for vertex positions. The index returned would be used as an index into the gm\_Matrices uniform within the shader code. |

The following constants are also available:

| Constant | Description |
| --- | --- |
| MATRICES\_MAX | The size of the matrix array (gm\_Matrices) in the vertex shader. |
| MAX\_VS\_LIGHTS | The maximum number of point and directional lights available in the vertex shader. |

## Uniforms

| Uniform | Shader | Description |
| --- | --- | --- |
| Common | | |
| gm\_Matrices\[matrix] | Vertex Shader | This array uniform of mat4s stores the various transform matrices used by GameMaker and is one of the available predefined uniforms that GameMaker creates for you to use within the shader code editor. The array index is chosen from one of the matrix index constants listed above, e.g. gm\_Matrices\[MATRIX\_WORLD\_VIEW\_PROJECTION]. Its number of elements is MATRICES\_MAX. |
| gm\_BaseTexture | Fragment Shader | This is a 2D sampler uniform that holds the texture of that which GameMaker is currently drawing. So it would be the (full) texture page the current sprite is on, the texture of the surface being drawn or the texture passed as the texture to [vertex\_submit](../../Drawing/Primitives/vertex_submit.md) in case you're submitting a custom vertex buffer. |
| Lighting | | |
| gm\_LightingEnabled | Vertex Shader | This boolean uniform holds whether lighting is enabled, i.e. the value set with [draw\_light\_enable](../../Drawing/Lighting/draw_light_enable.md) and returned by [draw\_get\_lighting](../../Drawing/Lighting/draw_get_lighting.md). |
| gm\_Lights\_Direction\[] | Vertex Shader | This is an array uniform of vec4s, where each vec4 contains a light's normalised direction vector (X, Y, Z) negated and a fourth dimension (W) which is 1 when the light is enabled, and 0 when disabled. Light properties can be set using [draw\_light\_define\_direction](../../Drawing/Lighting/draw_light_define_direction.md). |
| gm\_Lights\_PosRange\[] | Vertex Shader | This is an array uniform of vec4s, where each vec4 contains a light's position (X, Y, Z) and a fourth dimension (W) which is the light's range, which is 0 when that light is disabled. Light properties can be set using [draw\_light\_define\_point](../../Drawing/Lighting/draw_light_define_point.md). |
| gm\_Lights\_Colour\[] | Vertex Shader | This is an array uniform of vec4s, where each vec4 contains a light's colour (R, G, B), with the alpha channel (A) always being 1\. |
| gm\_AmbientColour | Vertex Shader | This is a vec4 uniform containing the colour of the ambient light as set with [draw\_light\_define\_ambient](../../Drawing/Lighting/draw_light_define_ambient.md). |
| Fog | | |
| gm\_FogStart | Vertex Shader | This is the distance where polygons start to be blended with the fog colour. |
| gm\_RcpFogRange | Vertex Shader | This is the distance at which fog is maximal and nothing can be seen anymore. |
| gm\_PS\_FogEnabled | Fragment Shader | This will hold true or false, depending on whether the GPU has pixel fog enabled or not. |
| gm\_FogColour | Fragment Shader | This can be used to get the fog colour used by GameMaker. |
| gm\_VS\_FogEnabled | Vertex Shader | This will hold true or false, depending on whether the GPU has vertex fog enabled or not. |
| Alpha Testing | | |
| gm\_AlphaTestEnabled | Fragment Shader | This boolean uniform holds whether alpha testing is enabled. See [gpu\_set\_alphatestenable](../../Drawing/GPU_Control/gpu_set_alphatestenable.md) for more information on alpha testing. |
| gm\_AlphaRefValue | Fragment Shader | This float uniform holds the current alpha testing reference value. See [gpu\_set\_alphatestref](../../Drawing/GPU_Control/gpu_set_alphatestref.md) for more information on the alpha test reference. |
