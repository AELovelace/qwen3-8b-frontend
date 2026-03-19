# flexpanel\_node\_style\_get\_display

This function returns the display property of the given [Flex Panel Node](../flexpanel_create_node.md).

See: [Display](../../Flex_Panels_Styling.md#h4) / [flexpanel\_node\_style\_set\_display](flexpanel_node_style_set_display.md)

 

#### Syntax:

flexpanel\_node\_style\_get\_display(node)

| Argument | Type | Description |
| --- | --- | --- |
| node | [Flex Panel Node](../flexpanel_create_node.md) | The node to read. |

 

#### Returns:

[Flex Panel Display Type Constant](flexpanel_node_style_set_display.md)

 

#### Example:

var \_display \= flexpanel\_node\_style\_get\_display(\_node);

This gets the display mode of a node and stores it in a local variable.
