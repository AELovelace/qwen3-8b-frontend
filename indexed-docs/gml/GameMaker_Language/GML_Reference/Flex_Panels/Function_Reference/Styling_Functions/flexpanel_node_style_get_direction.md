# flexpanel\_node\_style\_get\_direction

This function returns the direction property of the given [Flex Panel Node](../flexpanel_create_node.md).

See: [Layout Direction](../../Flex_Panels_Styling.md#layout) / [flexpanel\_node\_style\_set\_direction](flexpanel_node_style_set_direction.md)

 

#### Syntax:

flexpanel\_node\_style\_get\_direction(node)

| Argument | Type | Description |
| --- | --- | --- |
| node | [Flex Panel Node](../flexpanel_create_node.md) | The node to read. |

 

#### Returns:

[Flex Panel Layout Direction Constant](flexpanel_node_style_set_direction.md)

 

#### Example:

var \_layout\_direction \= flexpanel\_node\_style\_get\_direction(\_node);

This gets the layout direction of a node and stores it in a local variable.
