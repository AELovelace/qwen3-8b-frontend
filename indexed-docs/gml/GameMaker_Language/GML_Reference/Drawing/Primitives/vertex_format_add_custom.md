# vertex\_format\_add\_custom

This function adds a custom data type for specific vertex format attributes as part of the new vertex format being created.

The available values to use are defined by the data type constant that you choose, listed below: 

| [Vertex Data Type Constant](vertex_format_add_custom.md) | |
| --- | --- |
| Constant | Description |
| vertex\_type\_float1 | A single floating point value |
| vertex\_type\_float2 | Two floating point values |
| vertex\_type\_float3 | Three floating point values |
| vertex\_type\_float4 | Four floating point values |
| vertex\_type\_colour | Four component values (r, g, b, a) |
| vertex\_type\_ubyte4 | Four component unsigned byte values (from 0 to 255\) |

 
The use that these constants will be put to also needs to be defined so that the values can be "bound" properly within the shader being created. This is necessary due to the fact that DirectX and OpenGL have different requirements so if you don't bind them properly, they won't come through right in the shader. The available usage constants that you can choose from are listed below and those you use will depend on the specifics of the shader being created: 

| [Vertex Usage Type Constant](vertex_format_add_custom.md) | |
| --- | --- |
| Constant | Description |
| vertex\_usage\_position | position values (x, y, z) |
| vertex\_usage\_colour | colour values (r, g, b, a) |
| vertex\_usage\_normal | vertex normal values (nx, ny, nz) |
| vertex\_usage\_texcoord | UV coordinates (u, v) |
| vertex\_usage\_blendweight | the blendweight of the input matrix (for skeletal animation, for example) |
| vertex\_usage\_blendindices | the indices of the matrices to use (for skeletal animation, for example) |
| vertex\_usage\_depth | vertex depth buffer value |
| vertex\_usage\_tangent | tangent values |
| vertex\_usage\_binormal | binormal values |
| vertex\_usage\_fog | fog values |
| vertex\_usage\_sample | sampler index |

  

 There are some important things to note when using custom formats like these:

- The vertex\_format\_add\_custom function only supports vertex\_usage\_position, vertex\_usage\_colour, vertex\_usage\_normal and vertex\_usage\_texcoord when using GLSL shaders. These will map to the shader attributes in\_Position, in\_Colour\[0 \- ...], in\_Normal respectively (anything that is not one of these three attributes \- e.g.: texture coordinates \- can be mapped to any attribute you define).
- In general, you should use vertex\_usage\_texcoord for all extra parameters where possible, as types like vertex\_usage\_blendweight and vertex\_usage\_tangent are close to deprecated in most shader languages, and probably won't convert properly. Instead use vec, vec2, vec3 or vec4 types vertex\_usage\_texcoord and everything should work fine.
- GLSL ES does *not* support integer attributes, so passing in ivec4's does not work (this type is usually used when passing in vertex\_usage\_blendindices). What you need to do is pass in texture coordinates and then in the shader, convert them to ivec4 like this:

attribute vec3 in\_Position;  

 attribute vec4 in\_BlendIndices;  

 attribute vec4 in\_BlendWeights;  

  

 varying vec4 v\_vColour;  

 varying mat4 v\_mat;  

  

 void main()  

 {  

     gl\_Position \= gm\_Matrices\[MATRIX\_WORLD\_VIEW\_PROJECTION] \* vec4( in\_Position.xyz, 1\.0\);  

     v\_vColour \= in\_BlendWeights;  

     ivec4 t \= ivec4(in\_BlendIndices);  

     v\_mat \= gm\_Matrices\[ t.x ];  

 }
 

- Blend weights are usually stored in an array and then accessed using blend indices, but you can see here that instead of defining in\_BlendIndices as an ivec4 attribute, it's a vec4, then cast to an ivec4 in the code. This is then used to index the array created using the gm\_Matrices (you can only access an array using an INT value \- not a float).

 

#### Syntax:

vertex\_format\_add\_custom(type, usage)

| Argument | Type | Description |
| --- | --- | --- |
| type | [Vertex Data Type Constant](vertex_format_add_custom.md) | The data type that this custom vertex data will hold (see the ***type constants*** listed above). |
| usage | [Vertex Usage Type Constant](vertex_format_add_custom.md) | The use that the data will get (see the ***usage constants*** listed above). |

 

#### Returns:

N/A

 

#### Example:

vertex\_format\_begin();  

 vertex\_format\_add\_texcoord();  

 vertex\_format\_add\_custom(vertex\_type\_float3, vertex\_usage\_position);  

 my\_format \= vertex\_format\_end();

The above code creates a new vertex format with just a texture coordinate and 3 custom floating point values for position. It then stores the format in the variable my\_format.
