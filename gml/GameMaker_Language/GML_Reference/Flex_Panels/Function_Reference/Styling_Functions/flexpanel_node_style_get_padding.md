# flexpanel\_node\_style\_get\_padding

This function returns the padding for the given edge(s) of a [Flex Panel Node](../flexpanel_create_node.md).

See: [Padding](../../Flex_Panels_Styling.md#h15) / [flexpanel\_node\_style\_set\_padding](flexpanel_node_style_set_padding.md)

 

#### Syntax:

flexpanel\_node\_style\_get\_padding(node, edge)

| Argument | Type | Description |
| --- | --- | --- |
| node | [Flex Panel Node](../flexpanel_create_node.md) | The node to read. |
| edge | [Flex Panel Edge Constant](flexpanel_node_style_set_padding.md) | The edge to get the padding for. |

 

#### Returns:

[Flex Panel Unit\-Value Struct](section_index.md#units)

 

#### Example:

var \_padding \= flexpanel\_node\_style\_get\_padding(\_node, flexpanel\_edge.all\_edges);

This gets the general padding of a node and stores it in a local variable.
