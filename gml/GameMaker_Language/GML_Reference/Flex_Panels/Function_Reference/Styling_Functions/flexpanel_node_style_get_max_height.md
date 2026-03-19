# flexpanel\_node\_style\_get\_max\_height

This function returns the maxHeight property of the given [Flex Panel Node](../flexpanel_create_node.md).

See: [Min/Max Width and Height](../../Flex_Panels_Styling.md#h18) / [flexpanel\_node\_style\_set\_max\_height](flexpanel_node_style_set_max_height.md)

 

#### Syntax:

flexpanel\_node\_style\_get\_max\_height(node)

| Argument | Type | Description |
| --- | --- | --- |
| node | [Flex Panel Node](../flexpanel_create_node.md) | The node to read. |

 

#### Returns:

[Flex Panel Unit\-Value Struct](section_index.md#units)

 

#### Example:

var \_max\_height \= flexpanel\_node\_style\_get\_max\_height(\_node);

This gets the maximum height of a node and stores it in a local variable.
