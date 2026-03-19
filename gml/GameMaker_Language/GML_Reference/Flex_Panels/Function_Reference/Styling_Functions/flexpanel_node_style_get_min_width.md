# flexpanel\_node\_style\_get\_min\_width

This function returns the minWidth property of the given [Flex Panel Node](../flexpanel_create_node.md).

See: [Min/Max Width and Height](../../Flex_Panels_Styling.md#h18) / [flexpanel\_node\_style\_set\_min\_width](flexpanel_node_style_set_min_width.md)

 

#### Syntax:

flexpanel\_node\_style\_get\_min\_width(node)

| Argument | Type | Description |
| --- | --- | --- |
| node | [Flex Panel Node](../flexpanel_create_node.md) | The node to read. |

 

#### Returns:

[Flex Panel Unit\-Value Struct](section_index.md#units)

 

#### Example:

var \_min\_width \= flexpanel\_node\_style\_get\_min\_width(\_node);

This gets the minimum width of a node and stores it in a local variable.
