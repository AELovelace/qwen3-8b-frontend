# vertex\_update\_buffer\_from\_vertex

This function updates the contents of a vertex buffer using (part of) the contents of another vertex buffer.

  You cannot pass [frozen](vertex_freeze.md) vertex buffers into this function.

### Usage Notes

- You can optionally provide the starting vertex and the number of vertices to copy.
- The destination vertex buffer's [vertex format](Primitives_And_Vertex_Formats.md#func_ref_vertex_formats) should have the same attributes as the source vertex buffer (its [Vertex Format](vertex_format_end.md) can be different).
- If the destination vertex buffer never had any vertices added to it, the vertices will be added using the source buffer's vertex format.
- Writing data outside of the vertex buffer's current size will resize the vertex buffer as required.

 

#### Syntax:

vertex\_update\_buffer\_from\_vertex(dest\_vbuff, dest\_vert, src\_vbuff\[, src\_vert, src\_vert\_num])

| Argument | Type | Description |
| --- | --- | --- |
| dest\_vbuff | [Vertex Buffer](vertex_create_buffer.md) | The destination vertex buffer to copy vertices to |
| dest\_vert | [Real](../../../GML_Overview/Data_Types.md) | The index of the first vertex in the destination vertex buffer to copy to |
| src\_vbuff | [Vertex Buffer](vertex_create_buffer.md) | The source vertex buffer to copy vertices from |
| src\_vert | [Real](../../../GML_Overview/Data_Types.md) | The index of the first vertex in the source vertex buffer to copy |
| src\_vert\_num | [Real](../../../GML_Overview/Data_Types.md) | The number of vertices to copy |

 

#### Returns:

N/A

 

#### Example:

Create Event

vertex\_format\_begin();  

 vertex\_format\_add\_position\_3d();     // Three buffer\_f32 values  

 vertex\_format\_add\_color();           // Four buffer\_u8 values  

 vertex\_format\_add\_texcoord();        // Two buffer\_f32 values  

 vertex\_format \= vertex\_format\_end();  

  

 vb \= vertex\_create\_buffer();  

 vertex\_begin(vb, vertex\_format);  

 vertex\_position\_3d(vb, 100, 100, 0\);  

 vertex\_color(vb, c\_lime, 1\);  

 vertex\_texcoord(vb, 0, 0\);  

 vertex\_position\_3d(vb, 200, 100, 0\);  

 vertex\_color(vb, c\_lime, 1\);  

 vertex\_texcoord(vb, 1, 0\);  

 vertex\_position\_3d(vb, 200, 200, 0\);  

 vertex\_color(vb, c\_lime, 1\);  

 vertex\_texcoord(vb, 1, 1\);  

 vertex\_end(vb);  

  

 vb2 \= vertex\_create\_buffer();  

  

vertex\_update\_buffer\_from\_vertex(vb2, 0, vb);
 

Draw Event

vertex\_submit(vb2, pr\_trianglelist, \-1\);

The above code shows how to duplicate a vertex buffer's contents to another, newly created vertex buffer.

First, in the Create event, a vertex format identical to the [Passthrough Vertex Format](Primitives_And_Vertex_Formats.md#passthrough_vertex_format) is created and stored in a variable vertex\_format. Then, a new vertex buffer is created and filled with three vertices, according to the vertex format. After that, a second vertex buffer vb2 is created and updated with the vertex data in vb using vertex\_update\_buffer\_from\_vertex. After the function call, the vertex data in vb2 will be identical to that in vb.

Finally, in the Draw event, vb2 is drawn using [vertex\_submit](vertex_submit.md).
