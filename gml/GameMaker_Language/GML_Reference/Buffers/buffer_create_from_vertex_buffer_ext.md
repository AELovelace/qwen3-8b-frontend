# buffer\_create\_from\_vertex\_buffer\_ext

This function allocates a portion of memory as a buffer in your game and fills it with the vertex data of a range of vertices from a previously created [vertex buffer](../Drawing/Primitives/Primitives_And_Vertex_Formats.md).

The function returns a reference to the buffer that should be stored in a variable and used for all further function calls to the buffer. The function takes a reference to the vertex buffer to use (as returned by the function [vertex\_create\_buffer](../Drawing/Primitives/vertex_create_buffer.md), for example) with the following constants being used to define the buffer type:

 
Apart from the buffer type, you will also have to set the *byte alignment* for the buffer. This value will vary depending on the data that you wish to store in the buffer, and in most cases a value of 1 is perfectly fine. However, be aware that for some operations a specific alignment is *essential*, and an incorrect alignment may cause errors (for further details on alignment see [Buffer Alignment](../../../Additional_Information/Guide_To_Using_Buffers.md)). The following is a general guide to show which values are most appropriate for each data type (when in doubt, use an alignment of 1\):

- Strings should be aligned to 1 byte.
- Signed or unsigned 8bit integers can be aligned to any value, but note that for a fast buffer (see [buffer\_write](buffer_write.md)) it *must* be aligned to 1\.
- Signed or unsigned 16bit integers should be aligned to 2 bytes.
- Signed or unsigned 32bit integers should be aligned to 4 bytes
- Floats of up to 16bits should be aligned to 2 bytes.
- Floats of up to 32bits should be aligned to 4 bytes.
- Floats of up to 64bits should be aligned to 8 bytes.

The final two arguments are used to specify the range of vertex data that you wish to copy into the newly created buffer. The start vertex can be anywhere between 0 and the number of vertices \-1, and then you give the number of vertices from that point to copy. You can use the function [vertex\_get\_number](../Drawing/Primitives/vertex_get_number.md) on the vertex buffer to get the total number of vertices stored.

 Vertex buffers are 1 byte aligned, but you can create the buffer with any alignment depending on how you want to treat the data, as the vertex data is simply a raw memory copy into the buffer.

 
 

#### Syntax:

buffer\_create\_from\_vertex\_buffer\_ext(vertex\_buffer, type, alignment, start\_vertex, num\_vertices)

| Argument | Type | Description |
| --- | --- | --- |
| vertex\_buffer | [Vertex Buffer](../../../../GameMaker_Language/GML_Reference/Drawing/Primitives/vertex_create_buffer.md) | A reference to the vertex buffer to use. |
| type | [Buffer Type Constant](../../../../GameMaker_Language/GML_Reference/Buffers/buffer_create.md) | The type of buffer to create (see the constants list below). |
| alignment | [Real](../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The byte alignment for the buffer. |
| start\_vertex | [Real](../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The starting vertex. |
| num\_vertices | [Real](../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The total number of vertices to copy. |

 

#### Returns:

[Buffer](../../../../GameMaker_Language/GML_Reference/Buffers/buffer_create.md)

 

#### Example:

var \_v\_num \= vertex\_get\_number(model\_buff);  

 player\_buffer \= buffer\_create\_from\_vertex\_buffer\_ext(model\_buffer, buffer\_grow, 1, 0, \_v\_num \- 1\);

The above code allocates memory to a buffer then copies the data of all vertices from the given vertex buffer into it, returning the new buffer. It is stored in the variable player\_buffer for future use.
