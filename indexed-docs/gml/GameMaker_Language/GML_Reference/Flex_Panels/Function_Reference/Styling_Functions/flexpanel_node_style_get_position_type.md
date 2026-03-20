# flexpanel\_node\_style\_get\_position\_type

This function returns the position property of the given [Flex Panel Node](../flexpanel_create_node.md).

See: [Position Type](../../Flex_Panels_Styling.md#h17) / [flexpanel\_node\_style\_set\_position\_type](flexpanel_node_style_set_position_type.md)

 

#### Syntax:

flexpanel\_node\_style\_get\_position\_type(node)

| Argument | Type | Description |
| --- | --- | --- |
| node | [Flex Panel Node](../flexpanel_create_node.md) | The node to read. |

 

#### Returns:

[Flex Panel Position Type Constant](flexpanel_node_style_set_position_type.md)

 

#### Example:

var \_position\_type \= flexpanel\_node\_style\_get\_position\_type(\_node);

This gets the position type of a node and stores it in a local variable.
