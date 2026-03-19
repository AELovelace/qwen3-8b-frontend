# flexpanel\_node\_style\_set\_width

This function sets the width property of the given [Flex Panel Node](../flexpanel_create_node.md).

See: [Width and Height](../../Flex_Panels_Styling.md#h19)

 

#### Syntax:

flexpanel\_node\_style\_set\_width(node, width, unit)

| Argument | Type | Description |
| --- | --- | --- |
| node | [Flex Panel Node](../flexpanel_create_node.md) | The node to modify |
| width | [Real](../../../../GML_Overview/Data_Types.md) | The width to set |
| --- | --- | --- |
| unit | [Flex Panel Unit Constant](section_index.md#units) | The unit to use for the width |

 

#### Returns:

N/A

 

#### Example:

flexpanel\_node\_style\_set\_width(\_node, 100, flexpanel\_unit.percent);

This sets the width of a node to 100%.
