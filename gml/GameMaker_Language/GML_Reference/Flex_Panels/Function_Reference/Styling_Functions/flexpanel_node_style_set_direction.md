# flexpanel\_node\_style\_set\_direction

This function sets the direction property of the given [Flex Panel Node](../flexpanel_create_node.md). It can be one of the following enum members:

| Constant | Property Value |
| --- | --- |
| flexpanel\_direction.inherit | Inherit layout direction from parent |
| flexpanel\_direction.LTR | "ltr" |
| flexpanel\_direction.RTL | "rtl" |

See: [Layout Direction](../../Flex_Panels_Styling.md#layout)

 

#### Syntax:

flexpanel\_node\_style\_set\_direction(node, direction)

| Argument | Type | Description |
| --- | --- | --- |
| node | [Flex Panel Node](../flexpanel_create_node.md) | The node to modify |
| direction | [Flex Panel Layout Direction Constant](flexpanel_node_style_set_direction.md) | The layout direction to use |
| --- | --- | --- |

 

#### Returns:

N/A

 

#### Example:

flexpanel\_node\_style\_set\_direction(\_node, flexpanel\_direction.RTL);

This sets the layout direction of a node to right\-to\-left.
