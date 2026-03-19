# flexpanel\_node\_style\_set\_align\_items

This function sets the alignItems property of the given [Flex Panel Node](../flexpanel_create_node.md). It can be one of the following enum members:

| Constant | Property Value |
| --- | --- |
| flexpanel\_align.stretch | "stretch" |
| flexpanel\_align.flex\_start | "flex\_start" |
| flexpanel\_align.flex\_end | "flex\_end" |
| flexpanel\_align.center | "center" |
| flexpanel\_align.baseline | "baseline" |

See: [Align Items](../../Flex_Panels_Styling.md#h1)

 

#### Syntax:

flexpanel\_node\_style\_set\_align\_items(node, align)

| Argument | Type | Description |
| --- | --- | --- |
| node | [Flex Panel Node](../flexpanel_create_node.md) | The node to modify |
| align | [Flex Panel Alignment Constant](flexpanel_node_style_set_align_items.md) | The alignment to use |
| --- | --- | --- |

 

#### Returns:

N/A

 

#### Example:

flexpanel\_node\_style\_set\_align\_items(\_node, flexpanel\_align.center);

This sets the align items of a node to center.
