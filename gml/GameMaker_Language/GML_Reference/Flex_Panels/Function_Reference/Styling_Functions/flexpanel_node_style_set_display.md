# flexpanel\_node\_style\_set\_display

This function sets the display property of the given [Flex Panel Node](../flexpanel_create_node.md). It can be one of the following enum members:

| Constant | Property Value |
| --- | --- |
| flexpanel\_display.flex | "flex" |
| flexpanel\_display.none | "none" |

See: [Display](../../Flex_Panels_Styling.md#h4)

 

#### Syntax:

flexpanel\_node\_style\_set\_display(node, display)

| Argument | Type | Description |
| --- | --- | --- |
| node | [Flex Panel Node](../flexpanel_create_node.md) | The node to modify |
| display | [Flex Panel Display Type Constant](flexpanel_node_style_set_display.md) | The display type to use |
| --- | --- | --- |

 

#### Returns:

N/A

 

#### Example:

flexpanel\_node\_style\_set\_display(\_node, flexpanel\_display.none);

This sets the display mode of a node to none, effectively disabling it.
