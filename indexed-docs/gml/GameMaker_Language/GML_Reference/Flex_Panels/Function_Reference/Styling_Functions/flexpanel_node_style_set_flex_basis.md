# flexpanel\_node\_style\_set\_flex\_basis

This function sets the flexBasis property of the given [Flex Panel Node](../flexpanel_create_node.md).

See: [Flex Basis](../../Flex_Panels_Styling.md#h7)

 

#### Syntax:

flexpanel\_node\_style\_set\_flex\_basis(node, value, unit)

| Argument | Type | Description |
| --- | --- | --- |
| node | [Flex Panel Node](../flexpanel_create_node.md) | The node to modify |
| value | [Real](../../../../GML_Overview/Data_Types.md) | The value to set |
| --- | --- | --- |
| unit | [Flex Panel Unit Constant](section_index.md#units) | The unit of the value |

 

#### Returns:

N/A

 

#### Example:

flexpanel\_node\_style\_set\_flex\_basis(\_node, 60, flexpanel\_unit.point);

This sets the flex basis of a node to 60px.
