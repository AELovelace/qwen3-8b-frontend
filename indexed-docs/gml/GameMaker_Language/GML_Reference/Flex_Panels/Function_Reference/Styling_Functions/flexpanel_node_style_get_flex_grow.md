# flexpanel\_node\_style\_get\_flex\_grow

This function returns the flexGrow property of the given [Flex Panel Node](../flexpanel_create_node.md).

See: [Flex Grow](../../Flex_Panels_Styling.md#h9) / [flexpanel\_node\_style\_set\_flex\_grow](flexpanel_node_style_set_flex_grow.md)

 

#### Syntax:

flexpanel\_node\_style\_get\_flex\_grow(node)

| Argument | Type | Description |
| --- | --- | --- |
| node | [Flex Panel Node](../flexpanel_create_node.md) | The node to read. |

 

#### Returns:

[Real](../../../../GML_Overview/Data_Types.md)

 

#### Example:

var \_flex\_grow \= flexpanel\_node\_style\_get\_flex\_grow(\_node);

This gets the flex grow value of a node and stores it in a local variable.
