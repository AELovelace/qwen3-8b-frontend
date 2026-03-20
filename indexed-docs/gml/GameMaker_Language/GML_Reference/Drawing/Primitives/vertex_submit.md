# vertex\_submit

This function submits the contents of a vertex buffer to the graphics pipeline for use with a shader.

You supply the vertex buffer, the base primitive type (see the constants below) and the texture to be used. The base primitive type is only used for assigning the order in which the vertices that you stored in the buffer are drawn and connected, but the actual data used for each of the vertices will be that which you defined when creating the vertex buffer.

 
### Usage Notes

- This function can only be used in the [Draw Events](../../../../The_Asset_Editors/Object_Properties/Draw_Events.md).
- The number of vertices in the vertex buffer must be in accordance with the primitive type you're using.
- You can use [vertex\_submit\_ext](vertex_submit_ext.md) instead to submit only a range of vertices in the vertex buffer.
- Triangle fans (pr\_trianglefan) are converted to pr\_trianglelist internally on platforms that don't support them when you call this function.

For a visual example of the different base primitives available, see the image below: 

 
 

#### Syntax:

vertex\_submit(buffer, primitive, texture)

| Argument | Type | Description |
| --- | --- | --- |
| buffer | [Vertex Buffer](vertex_create_buffer.md) | The vertex buffer to use. |
| primitive | [Primitive Type Constant](draw_primitive_begin.md) | The primitive base type. |
| texture | [Texture](../../Asset_Management/Sprites/Sprite_Information/sprite_get_texture.md) | The texture to use (or \-1 for no texture). |

 

#### Returns:

N/A

 

#### Example:

shader\_set(shader\_prim);  

vertex\_submit(buff, pr\_trianglelist, sprite\_get\_texture(sprite\_index, 0\));  

 shader\_reset();
 

The above code submits the vertex buffer in the variable buff for drawing with the shader shader\_prim, using a triangle list as the base primitive and the texture of the sprite for the instance running the code.
