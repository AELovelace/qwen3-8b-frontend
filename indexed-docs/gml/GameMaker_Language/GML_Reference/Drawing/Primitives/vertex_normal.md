# vertex\_normal

This function adds normal data to the vertex currently being defined for the custom primitive.

You supply the vertex buffer to write the data into as well as the x, y and z components of the normal.

 

#### Syntax:

vertex\_normal(buffer, nx, ny, nz)

| Argument | Type | Description |
| --- | --- | --- |
| buffer | [Vertex Buffer](../../../../../GameMaker_Language/GML_Reference/Drawing/Primitives/vertex_create_buffer.md) | The vertex buffer to write the information to. |
| nx | [Real](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The x component of the normal. |
| ny | [Real](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The y component of the normal. |
| nz | [Real](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The z component of the normal. |

 

#### Returns:

N/A

 

#### Example:

vertex\_normal(buff, 0, 1, 1\);

The above code will set the surface normal of the vertex being defined.
