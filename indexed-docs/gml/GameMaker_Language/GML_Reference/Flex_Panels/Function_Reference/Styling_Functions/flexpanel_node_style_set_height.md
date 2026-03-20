# flexpanel\_node\_style\_set\_height

This function sets the height property of the given [Flex Panel Node](../flexpanel_create_node.md).

See: [Width and Height](../../Flex_Panels_Styling.md#h19)

 

#### Syntax:

flexpanel\_node\_style\_set\_height(node, height, unit)

| Argument | Type | Description |
| --- | --- | --- |
| node | [Flex Panel Node](../flexpanel_create_node.md) | The node to modify |
| height | [Real](../../../../GML_Overview/Data_Types.md) | The height to set |
| --- | --- | --- |
| unit | [Flex Panel Unit Constant](section_index.md#units) | The unit to use for the height |

 

#### Returns:

N/A

 

#### Example:

flexpanel\_node\_style\_set\_height(\_node, 100, flexpanel\_unit.percent);

This sets the height of a node to 100%.
