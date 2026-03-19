# flexpanel\_node\_style\_set\_flex\_direction

This function sets the flexDirection property of the given [Flex Panel Node](../flexpanel_create_node.md). It can be one of the following enum members:

| Constant | Property Value |
| --- | --- |
| flexpanel\_flex\_direction.column | "column" |
| flexpanel\_flex\_direction.row | "row" |
| flexpanel\_flex\_direction.column\_reverse | "column\-reverse" |
| flexpanel\_flex\_direction.row\_reverse | "row\-reverse" |

See: [Flex Direction](../../Flex_Panels_Styling.md#h8)

 

#### Syntax:

flexpanel\_node\_style\_set\_flex\_direction(node, flex\_direction)

| Argument | Type | Description |
| --- | --- | --- |
| node | [Flex Panel Node](../flexpanel_create_node.md) | The node to modify |
| flex\_direction | [Flex Direction Constant](flexpanel_node_style_set_flex_direction.md) | The flex direction to set |
| --- | --- | --- |

 

#### Returns:

N/A

 

#### Example:

flexpanel\_node\_style\_set\_flex\_direction(\_node, flexpanel\_flex\_direction.column);

This sets the flex direction of a node to column.
