# flexpanel\_node\_style\_set\_padding

This function sets the padding for the given edge(s) of a [Flex Panel Node](../flexpanel_create_node.md). You can pass one of the following enum members for the edge:

| Constant | Property |
| --- | --- |
| flexpanel\_edge.left | "paddingLeft" |
| flexpanel\_edge.top | "paddingTop" |
| flexpanel\_edge.right | "paddingRight" |
| flexpanel\_edge.bottom | "paddingBottom" |
| flexpanel\_edge.start | "paddingStart" |
| flexpanel\_edge.end | "paddingEnd" |
| flexpanel\_edge.horizontal | "paddingHorizontal" |
| flexpanel\_edge.vertical | "paddingVertical" |
| flexpanel\_edge.all\_edges | "padding" |

See: [Padding](../../Flex_Panels_Styling.md#h15)

 

#### Syntax:

flexpanel\_node\_style\_set\_padding(node, edge, size, \[unit])

| Argument | Type | Description |
| --- | --- | --- |
| node | [Flex Panel Node](../flexpanel_create_node.md) | The node to modify |
| edge | [Flex Panel Edge Constant](flexpanel_node_style_set_padding.md) | The edge to set the padding for |
| --- | --- | --- |
| size | [Real](../../../../GML_Overview/Data_Types.md) | The size of the padding |
| unit | [Flex Panel Unit Constant](section_index.md#units) | The unit in which the padding is expressed. Defaults to flexpanel\_unit.point. |

 

#### Returns:

N/A

 

#### Example:

flexpanel\_node\_style\_set\_padding(\_node, flexpanel\_edge.all\_edges, 10\);

This sets the padding of a node for all its edges to 10px.
