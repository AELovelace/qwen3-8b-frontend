# flexpanel\_node\_style\_set\_min\_height

This function sets the minHeight property of the given [Flex Panel Node](../flexpanel_create_node.md).

See: [Min/Max Width and Height](../../Flex_Panels_Styling.md#h18)

 

#### Syntax:

flexpanel\_node\_style\_set\_min\_height(node, value, unit)

| Argument | Type | Description |
| --- | --- | --- |
| node | [Flex Panel Node](../flexpanel_create_node.md) | The node to modify |
| value | [Real](../../../../GML_Overview/Data_Types.md) | The value to use |
| --- | --- | --- |
| unit | [Flex Panel Unit Constant](section_index.md#units) | The unit of the value |

 

#### Returns:

N/A

 

#### Example:

flexpanel\_node\_style\_set\_min\_height(\_node, 60, flexpanel\_unit.point);

This sets the minimum height of a node to 60px.
