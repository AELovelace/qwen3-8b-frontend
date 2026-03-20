# flexpanel\_node\_style\_set\_margin

This function sets the margin for the given edge(s) of a [Flex Panel Node](../flexpanel_create_node.md).

See: [Margin](../../Flex_Panels_Styling.md#h14)

 

#### Syntax:

flexpanel\_node\_style\_set\_margin(node, edge, size, \[unit])

| Argument | Type | Description |
| --- | --- | --- |
| node | [Flex Panel Node](../flexpanel_create_node.md) | The node to modify |
| edge | [Flex Panel Edge Constant](flexpanel_node_style_set_padding.md) | The edge to set the margin of |
| --- | --- | --- |
| size | [Real](../../../../GML_Overview/Data_Types.md) | The size of the margin |
| unit | [Flex Panel Unit Constant](section_index.md#units) | The unit in which the margin is expressed. Defaults to flexpanel\_unit.point. |

 

#### Returns:

N/A

 

#### Example:

flexpanel\_node\_style\_set\_margin(\_node, flexpanel\_edge.all\_edges, 10\);

This sets the margin of a node for all its edges to 10px.
