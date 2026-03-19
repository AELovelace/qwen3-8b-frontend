# flexpanel\_node\_style\_set\_max\_width

This function sets the maxWidth property of the given [Flex Panel Node](../flexpanel_create_node.md).

See: [Min/Max Width and Height](../../Flex_Panels_Styling.md#h18)

 

#### Syntax:

flexpanel\_node\_style\_set\_max\_width(node, value, unit)

| Argument | Type | Description |
| --- | --- | --- |
| node | [Flex Panel Node](../flexpanel_create_node.md) | The node to modify |
| value | [Real](../../../../GML_Overview/Data_Types.md) | The value to use |
| --- | --- | --- |
| unit | [Flex Panel Unit Constant](section_index.md#units) | The unit of the value |

 

#### Returns:

N/A

 

#### Example:

flexpanel\_node\_style\_set\_max\_width(\_node, 400, flexpanel\_unit.point);

This sets the maximum width of a node to 400px.
