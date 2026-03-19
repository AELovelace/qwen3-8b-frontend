# flexpanel\_node\_style\_get\_width

This function returns the width property of the given [Flex Panel Node](../flexpanel_create_node.md).

See: [Width and Height](../../Flex_Panels_Styling.md#h19) / [flexpanel\_node\_style\_set\_width](flexpanel_node_style_set_width.md)

 

#### Syntax:

flexpanel\_node\_style\_get\_width(node)

| Argument | Type | Description |
| --- | --- | --- |
| node | [Flex Panel Node](../flexpanel_create_node.md) | The node to read. |

 

#### Returns:

[Flex Panel Unit\-Value Struct](section_index.md#units)

 

#### Example:

var \_width \= flexpanel\_node\_style\_get\_width(\_node);

This gets the width of a node and stores it in a local variable.
