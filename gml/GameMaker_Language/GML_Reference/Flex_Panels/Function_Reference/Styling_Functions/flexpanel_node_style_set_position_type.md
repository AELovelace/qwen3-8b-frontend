# flexpanel\_node\_style\_set\_position\_type

This function sets the position property of the given [Flex Panel Node](../flexpanel_create_node.md). It can be one of the following enum members:

| Constant | Property Value |
| --- | --- |
| flexpanel\_position\_type.relative | "relative" |
| flexpanel\_position\_type.absolute | "absolute" |
| flexpanel\_position\_type.static | "static" |

See: [Position Type](../../Flex_Panels_Styling.md#h17)

 

#### Syntax:

flexpanel\_node\_style\_set\_position\_type(node, position\_type)

| Argument | Type | Description |
| --- | --- | --- |
| node | [Flex Panel Node](../flexpanel_create_node.md) | The node to modify |
| position\_type | [Flex Panel Position Type Constant](flexpanel_node_style_set_position_type.md) | The position type to set |
| --- | --- | --- |

 

#### Returns:

N/A

 

#### Example:

flexpanel\_node\_style\_set\_position\_type(\_node, flexpanel\_position\_type.absolute);  

flexpanel\_node\_style\_set\_position(\_node, flexpanel\_edge.left, 20, flexpanel\_unit.point);  

flexpanel\_node\_style\_set\_position(\_node, flexpanel\_edge.top, 40, flexpanel\_unit.point);
 

This sets a node's position type to absolute, and then sets the left position to 20px and top position to 40px.
