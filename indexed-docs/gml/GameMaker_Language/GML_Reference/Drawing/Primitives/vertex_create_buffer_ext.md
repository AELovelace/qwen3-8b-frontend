# vertex\_create\_buffer\_ext

This function creates a new vertex buffer and sets its initial size in bytes.

This is a special *grow* buffer created by GameMaker which is pre\-formatted for use when building primitives for use with shaders. You can specify an initial starting size for the buffer (in bytes) and it will return an index for the buffer which should then be used in all further calls to the buffer.

 

#### Syntax:

vertex\_create\_buffer\_ext(size)

| Argument | Type | Description |
| --- | --- | --- |
| size | [Real](../../../GML_Overview/Data_Types.md) | The initial size of the buffer (in bytes) |

 

#### Returns:

[Vertex Buffer](vertex_create_buffer.md)

 

#### Example:

v\_buff \= vertex\_create\_buffer\_ext(1024 \* 1024\);

The above code creates a new vertex buffer, initially 1MB in size, and store it in the variable v\_buff.
