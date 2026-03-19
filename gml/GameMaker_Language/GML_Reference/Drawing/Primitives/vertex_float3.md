# vertex\_float3

This function adds three floating point values to the vertex data.

The vertex buffer must have been formatted correctly to accept this using the [vertex\_format\_add\_custom](vertex_format_add_custom.md)
 function.
 

 

#### Syntax:

vertex\_float3(buffer, float, float, float)

| Argument | Type | Description |
| --- | --- | --- |
| buffer | [Vertex Buffer](../../../../../GameMaker_Language/GML_Reference/Drawing/Primitives/vertex_create_buffer.md) | The vertex buffer to write the information to. |
| float | [Real](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The first input value. |
| float | [Real](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The second input value. |
| float | [Real](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The third input value. |

 

#### Returns:

N/A

 

#### Example:

vertex\_float3(buff, 0\.05, 0\.01, room\_width / x);

The above code adds three floating point values to the vertex data being defined.
