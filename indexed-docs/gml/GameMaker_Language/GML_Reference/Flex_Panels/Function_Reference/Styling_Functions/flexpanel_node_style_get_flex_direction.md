# flexpanel\_node\_style\_get\_flex\_direction

This function returns the flexDirection property of the given [Flex Panel Node](../flexpanel_create_node.md).

See: [Flex Direction](../../Flex_Panels_Styling.md#h8) / [flexpanel\_node\_style\_set\_flex\_direction](flexpanel_node_style_set_flex_direction.md)

 

#### Syntax:

flexpanel\_node\_style\_get\_flex\_direction(node)

| Argument | Type | Description |
| --- | --- | --- |
| node | [Flex Panel Node](../flexpanel_create_node.md) | The node to read. |

 

#### Returns:

[Flex Direction Constant](flexpanel_node_style_set_flex_direction.md)

 

#### Example:

var \_flex\_direction \= flexpanel\_node\_style\_get\_flex\_direction(\_node);

This gets the flex direction of a node and stores it in a local variable.
