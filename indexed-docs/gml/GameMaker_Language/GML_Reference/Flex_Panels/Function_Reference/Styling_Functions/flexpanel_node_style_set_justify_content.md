# flexpanel\_node\_style\_set\_justify\_content

This function sets the justifyContent property of the given [Flex Panel Node](../flexpanel_create_node.md). It can be one of the following enum members:

| Constant | Property Value |
| --- | --- |
| flexpanel\_justify.start | "flex\-start" |
| flexpanel\_justify.flex\_end | "flex\-end" |
| flexpanel\_justify.center | "center" |
| flexpanel\_justify.space\_between | "space\-between" |
| flexpanel\_justify.space\_around | "space\-around" |
| flexpanel\_justify.space\_evenly | "space\-evenly" |

See: [Justify Content](../../Flex_Panels_Styling.md#h13)

 

#### Syntax:

flexpanel\_node\_style\_set\_justify\_content(node, justify)

| Argument | Type | Description |
| --- | --- | --- |
| node | [Flex Panel Node](../flexpanel_create_node.md) | The node to modify |
| justify | [Flex Panel Justify Content Constant](flexpanel_node_style_set_justify_content.md) | The justification to use |
| --- | --- | --- |

 

#### Returns:

N/A

 

#### Example:

flexpanel\_node\_style\_set\_justify\_content(\_node, flexpanel\_justify.space\_between);

This sets the justify content of a node to space\-between.
