# vertex\_float1

This function adds a floating point value to the vertex data.

The vertex buffer must have been formatted correctly to accept this using the [vertex\_format\_add\_custom](vertex_format_add_custom.md) function.

 

#### Syntax:

vertex\_float1(buffer, float)

| Argument | Type | Description |
| --- | --- | --- |
| buffer | [Vertex Buffer](../../../../../GameMaker_Language/GML_Reference/Drawing/Primitives/vertex_create_buffer.md) | The vertex buffer to write the information to. |
| float | [Real](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The input value. |

 

#### Returns:

N/A

 

#### Example:

vertex\_float1(buff, 0\.05\);

The above code adds a floating point value to the vertex data being defined.
