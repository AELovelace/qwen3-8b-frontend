# vertex\_position\_3d

This function adds 3D position data to the vertex currently being defined for the custom primitive.

You supply the vertex buffer to write the data into as well as the x, y and z components of the vertex position.

 

#### Syntax:

vertex\_position\_3d(buffer, x, y, z)

| Argument | Type | Description |
| --- | --- | --- |
| buffer | [Vertex Buffer](../../../../../GameMaker_Language/GML_Reference/Drawing/Primitives/vertex_create_buffer.md) | The vertex buffer to write the information to. |
| x | [Real](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The x position. |
| y | [Real](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The y position. |
| z | [Real](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The z position. |

 

#### Returns:

N/A

 

#### Example:

vertex\_position\_3d(buff, x \- 100, y \- 125, 0\);

The above code sets the position of the vertex being defined.
