# flexpanel\_node\_style\_get\_flex\_basis

This function returns the flexBasis property of the given [Flex Panel Node](../flexpanel_create_node.md).

See: [Flex Basis](../../Flex_Panels_Styling.md#h7) / [flexpanel\_node\_style\_set\_flex\_basis](flexpanel_node_style_set_flex_basis.md)

 

#### Syntax:

flexpanel\_node\_style\_get\_flex\_basis(node)

| Argument | Type | Description |
| --- | --- | --- |
| node | [Flex Panel Node](../flexpanel_create_node.md) | The node to read. |

 

#### Returns:

[Flex Panel Unit\-Value Struct](section_index.md#units)

 

#### Example:

var \_flex\_basis \= flexpanel\_node\_style\_get\_flex\_basis(\_node);

This gets the flex basis value of a node and stores it in a local variable.
