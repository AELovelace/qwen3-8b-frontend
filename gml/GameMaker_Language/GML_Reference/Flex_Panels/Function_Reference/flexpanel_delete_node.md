# flexpanel\_delete\_node

This function deletes the given [Flex Panel Node](flexpanel_create_node.md). You can choose whether it should also delete all of its child nodes, which it won't do by default.

 

#### Syntax:

flexpanel\_delete\_node(node, \[recursive])

| Argument | Type | Description |
| --- | --- | --- |
| node | [Flex Panel Node](flexpanel_create_node.md) | The node to delete |
| recursive | [Boolean](../../../GML_Overview/Data_Types.md) | Whether to delete all child nodes (true) or not (false, default) |

 

#### Returns:

N/A

 

#### Example:

flexpanel\_delete\_node(n\_root, true);

This deletes the node n\_root and all of its children.
