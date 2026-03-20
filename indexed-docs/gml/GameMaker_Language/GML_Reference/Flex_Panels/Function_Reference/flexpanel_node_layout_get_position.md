# flexpanel\_node\_layout\_get\_position

This function returns a struct with the layout information of the given node. You must have called [flexpanel\_calculate\_layout](flexpanel_calculate_layout.md) at least once on the node before calling this, otherwise all returned data will be 0\.

By default, the returned position will be relative to the position of the parent container. You can pass false to the relative argument to instead return the absolute position of the node, after applying all parent transformations.

The left, top, width and height members are the ones that are most useful for making use of the calculated layouts (e.g. creating an object instance, drawing a rectangle, etc.).

The returned struct will contain the following members:

| Member | Data Type | Description |
| --- | --- | --- |
| left | [Real](../../../GML_Overview/Data_Types.md) | The calculated X position of the left edge of the node |
| top | [Real](../../../GML_Overview/Data_Types.md) | The calculated Y position of the top edge of the node |
| width | [Real](../../../GML_Overview/Data_Types.md) | The width of the node |
| height | [Real](../../../GML_Overview/Data_Types.md) | The height of the node |
| bottom | [Real](../../../GML_Overview/Data_Types.md) | The position of the bottom edge of the node, relative to the bottom edge of its parent container |
| right | [Real](../../../GML_Overview/Data_Types.md) | The position of the right edge of the node, relative to the right edge of its parent container |
| hadOverflow | [Boolean](../../../GML_Overview/Data_Types.md) | A boolean indicating whether any child nodes have overflown outside of the bounds of the node |
| direction | [Flex Panel Layout Direction Constant](Styling_Functions/flexpanel_node_style_set_direction.md) | The layout direction used for this node |
| paddingLeft | [Real](../../../GML_Overview/Data_Types.md) | The left edge's padding value |
| paddingRight | [Real](../../../GML_Overview/Data_Types.md) | The right edge's padding value |
| paddingTop | [Real](../../../GML_Overview/Data_Types.md) | The top edge's padding value |
| paddingBottom | [Real](../../../GML_Overview/Data_Types.md) | The bottom edge's padding value |
| marginLeft | [Real](../../../GML_Overview/Data_Types.md) | The left edge's margin value |
| marginRight | [Real](../../../GML_Overview/Data_Types.md) | The right edge's margin value |
| marginTop | [Real](../../../GML_Overview/Data_Types.md) | The top edge's margin value |
| marginBottom | [Real](../../../GML_Overview/Data_Types.md) | The bottom edge's margin value |

 

#### Syntax:

flexpanel\_node\_layout\_get\_position(node, \[relative])

| Argument | Type | Description |
| --- | --- | --- |
| node | [Flex Panel Node](flexpanel_create_node.md) | The node to get the layout position of |
| relative | [Boolean](../../../GML_Overview/Data_Types.md) | Whether to return relative positions (true, default) or absolute positions (false) |

 

#### Returns:

[Struct](../../../GML_Overview/Structs.md)

 

#### Example:
