# vertex\_create\_buffer\_from\_buffer\_ext

This function creates a new vertex buffer by copying the data from the buffer that is specified as the source.

The data in the source buffer must be pre\-formatted according to the vertex format for building primitives for use with (for example) shaders, and you can also supply an offset within the source buffer to copy from and the number of vertices that the final buffer should have.

  If the number of vertices does not match those being copied you may get corrupted vertex data.

 

#### Syntax:

vertex\_create\_buffer\_from\_buffer\_ext(buffer, format, src\_offset, vert\_num)

| Argument | Type | Description |
| --- | --- | --- |
| buffer | [Buffer](../../../../../GameMaker_Language/GML_Reference/Buffers/buffer_create.md) | The buffer to create the vertex buffer from. |
| format | [Primitive Type Constant](../../../../../GameMaker_Language/GML_Reference/Drawing/Primitives/draw_primitive_begin.md) | The primitive vertex format to use. |
| src\_offset | [Real](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The offset within the source buffer to copy from. |
| vert\_num | [Real](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The number of vertices the vertex buffer should have. |

 

#### Returns:

[Vertex Buffer](../../../../../GameMaker_Language/GML_Reference/Drawing/Primitives/vertex_create_buffer.md)

 

#### Example:

vertex\_format\_begin();  

 vertex\_format\_add\_position\_3d();  

 vertex\_format\_add\_colour();  

 vertex\_format\_add\_texcoord();  

 var my\_format \= vertex\_format\_end();  

 v\_buff \= vertex\_create\_buffer\_from\_buffer(global.modelBuff, myFormat, 0, 512\);

The above code will create a new vertex format then create a new vertex buffer from a previously created regular buffer, applying the custom vertex format to it with 0 offset. The function tells the new vertex buffer that it should expect 512 vertices.
