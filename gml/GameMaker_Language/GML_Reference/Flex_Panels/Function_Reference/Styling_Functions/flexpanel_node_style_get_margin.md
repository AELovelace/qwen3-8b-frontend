# flexpanel\_node\_style\_get\_margin

This function returns the margin for the given edge(s) of a [Flex Panel Node](../flexpanel_create_node.md).

See: [Margin](../../Flex_Panels_Styling.md#h14) / [flexpanel\_node\_style\_set\_margin](flexpanel_node_style_set_margin.md)

 

#### Syntax:

flexpanel\_node\_style\_get\_margin(node, edge)

| Argument | Type | Description |
| --- | --- | --- |
| node | [Flex Panel Node](../flexpanel_create_node.md) | The node to read. |
| edge | [Flex Panel Edge Constant](flexpanel_node_style_set_padding.md) | The edge to get the margin for. |

 

#### Returns:

[Flex Panel Unit\-Value Struct](section_index.md#units)

 

#### Example:

var \_margin \= flexpanel\_node\_style\_get\_margin(\_node, flexpanel\_edge.all\_edges);

This gets the general margin of a node and stores it in a local variable.
