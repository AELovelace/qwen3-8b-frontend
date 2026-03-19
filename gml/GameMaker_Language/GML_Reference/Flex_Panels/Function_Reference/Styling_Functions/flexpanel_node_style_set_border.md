# flexpanel\_node\_style\_set\_border

This function sets the border for the given edge(s) of a [Flex Panel Node](../flexpanel_create_node.md).

See: [Border](../../Flex_Panels_Styling.md#h16)

 

#### Syntax:

flexpanel\_node\_style\_set\_border(node, edge, size)

| Argument | Type | Description |
| --- | --- | --- |
| node | [Flex Panel Node](../flexpanel_create_node.md) | The node to modify |
| edge | [Flex Panel Edge Constant](flexpanel_node_style_set_padding.md) | The edge to set the border for |
| --- | --- | --- |
| size | [Real](../../../../GML_Overview/Data_Types.md) | The size of the border |

 

#### Returns:

N/A

 

#### Example:

flexpanel\_node\_style\_set\_border(\_node, flexpanel\_edge.all\_edges, 10\);

This sets the border of a node for all its edges to 10px.
