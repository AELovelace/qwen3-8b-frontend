# flexpanel\_calculate\_layout

This function calculates the layout data for the given node and all of its children. The calculated layouts are returned with [flexpanel\_node\_layout\_get\_position](flexpanel_node_layout_get_position.md).

It is required that you run this function at least once before using the layout positions of a node, otherwise all positions for the node (and its child nodes) will be 0\. You may run this function again for re\-calculating layouts in case of a resolution change.

The function takes a width and a height where the root node is "placed" for layout calculations. For example, if the root node has a [width](../Flex_Panels_Styling.md) of "100%", and the width you pass to this function is 560, then the width of that root node canvas becomes 560 pixels.

You can see these dimensions as the final resolution of the canvas where your layout is active, e.g. when making a full\-screen interface, these dimensions would be equal to your game window's size, or for an interface that is housed inside a small window within your game, they would be the dimensions of that window.

The width or height can be [undefined](../../../GML_Overview/Data_Types.md), in which case it will extend indefinitely.

You must choose whether the [layout direction](../Flex_Panels_Styling.md#layout) is left\-to\-right or right\-to\-left by passing a [Flex Panel Layout Direction Constant](Styling_Functions/flexpanel_node_style_set_direction.md).

 

#### Syntax:

flexpanel\_calculate\_layout(root, width, height, direction)

| Argument | Type | Description |
| --- | --- | --- |
| root | [Flex Panel Node](flexpanel_create_node.md) | The node for which calculations are performed |
| width | [Real](../../../GML_Overview/Data_Types.md) or [undefined](../../../GML_Overview/Data_Types.md) | The width that the root node is calculated against |
| height | [Real](../../../GML_Overview/Data_Types.md) or [undefined](../../../GML_Overview/Data_Types.md) | The height that the root node is calculated against |
| direction | [Flex Panel Layout Direction Constant](Styling_Functions/flexpanel_node_style_set_direction.md) | The direction to use for all nodes |

 

#### Returns:

N/A

 

#### Example:

flexpanel\_calculate\_layout(n\_root, room\_width, room\_height, flexpanel\_direction.LTR);

This calculates the layout for the node n\_root within the room dimensions, using a left\-to\-right direction.
