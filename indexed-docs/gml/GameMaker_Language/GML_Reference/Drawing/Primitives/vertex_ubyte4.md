# vertex\_ubyte4

This function adds four unsigned byte values (0 \- 255\) to the vertex data.

The vertex buffer must have been formatted correctly to accept this using the [vertex\_format\_add\_custom](vertex_format_add_custom.md) function.

 
 

#### Syntax:

vertex\_ubyte4(buffer, byte, byte, byte, byte)

| Argument | Type | Description |
| --- | --- | --- |
| buffer | [Vertex Buffer](vertex_create_buffer.md) | The vertex buffer to write the information to. |
| byte | [Real](../../../GML_Overview/Data_Types.md) | The first input value. |
| byte | [Real](../../../GML_Overview/Data_Types.md) | The second input value. |
| byte | [Real](../../../GML_Overview/Data_Types.md) | The third input value. |
| byte | [Real](../../../GML_Overview/Data_Types.md) | The fourth input value. |

 

#### Returns:

N/A

 

#### Example:

vertex\_ubyte4(buff, irandom(255\), irandom(255\), irandom(255\), 127\);

The above code adds four values to the vertex data being defined.
