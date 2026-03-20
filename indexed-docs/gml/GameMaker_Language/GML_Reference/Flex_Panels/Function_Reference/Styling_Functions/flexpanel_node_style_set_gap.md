# flexpanel\_node\_style\_set\_gap

This function sets the gap size of the given [Flex Panel Node](../flexpanel_create_node.md). You must supply the gutter where the gap is applied:

| Constant | Property |
| --- | --- |
| flexpanel\_gutter.all\_gutters | "gap" |
| flexpanel\_gutter.row | "gapRow" |
| flexpanel\_gutter.column | "gapColumn" |

See: [Gap](../../Flex_Panels_Styling.md#h11)

 

#### Syntax:

flexpanel\_node\_style\_set\_gap(node, gutter, size)

| Argument | Type | Description |
| --- | --- | --- |
| node | [Flex Panel Node](../flexpanel_create_node.md) | The node to modify |
| gutter | [Flex Panel Gutter Constant](flexpanel_node_style_set_gap.md) | The gutter to set |
| --- | --- | --- |
| size | [Real](../../../../GML_Overview/Data_Types.md) | The gutter size |

 

#### Returns:

N/A

 

#### Example:

flexpanel\_node\_style\_set\_gap(\_node, flexpanel\_gutter.all\_gutters, 10\);

This sets the gap of a node for all gutters to 10px.
