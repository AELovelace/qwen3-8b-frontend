# flexpanel\_node\_style\_get\_justify\_content

This function returns the justifyContent property of the given [Flex Panel Node](../flexpanel_create_node.md).

See: [Justify Content](../../Flex_Panels_Styling.md#h13) / [flexpanel\_node\_style\_set\_justify\_content](flexpanel_node_style_set_justify_content.md)

 

#### Syntax:

flexpanel\_node\_style\_get\_justify\_content(node)

| Argument | Type | Description |
| --- | --- | --- |
| node | [Flex Panel Node](../flexpanel_create_node.md) | The node to read. |

 

#### Returns:

[Flex Panel Justify Content Constant](flexpanel_node_style_set_justify_content.md)

 

#### Example:

var \_justify \= flexpanel\_node\_style\_get\_justify\_content(\_node);

This gets the justify content value of a node and stores it in a local variable.
