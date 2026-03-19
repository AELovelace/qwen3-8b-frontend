# flexpanel\_node\_style\_set\_flex\_wrap

This function sets the flexWrap property of the given [Flex Panel Node](../flexpanel_create_node.md). It can be one of the following enum members:

| Constant | Property Value |
| --- | --- |
| flexpanel\_wrap.no\_wrap | "no\-wrap" |
| flexpanel\_wrap.wrap | "wrap" |
| flexpanel\_wrap.reverse | "wrap\-reverse" |

See: [Flex Wrap](../../Flex_Panels_Styling.md#h6)

 

#### Syntax:

flexpanel\_node\_style\_set\_flex\_wrap(node, wrap)

| Argument | Type | Description |
| --- | --- | --- |
| node | [Flex Panel Node](../flexpanel_create_node.md) | The node to modify |
| wrap | [Flex Panel Wrap Constant](flexpanel_node_style_set_flex_wrap.md) | The wrap mode to use |
| --- | --- | --- |

 

#### Returns:

N/A

 

#### Example:

flexpanel\_node\_style\_set\_flex\_wrap(\_node, flexpanel\_wrap.wrap);

This enables wrapping for a node.
