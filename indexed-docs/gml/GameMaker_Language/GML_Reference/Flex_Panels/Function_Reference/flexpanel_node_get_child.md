# flexpanel\_node\_get\_child

This function looks for a child node in the given parent node and returns the child.

The function accepts either of two kinds of values, which is used to look for the child:

- The index of the child node, as passed into [flexpanel\_node\_insert\_child](flexpanel_node_insert_child.md) or a value from 0 to the value of [flexpanel\_node\_get\_num\_children](flexpanel_node_get_num_children.md) \- 1
- The name of the child node, which is originally set either through the name property in the [initial struct](flexpanel_create_node.md) or through [flexpanel\_node\_set\_name](flexpanel_node_set_name.md). This search is done recursively through all child nodes and the first matching node is returned.

The function will return [undefined](../../../GML_Overview/Data_Types.md) if the child was not found (e.g. the index was out of range or name was not found).

 

#### Syntax:

flexpanel\_node\_get\_child(node, index\_or\_name)

| Argument | Type | Description |
| --- | --- | --- |
| node | [Flex Panel Node](flexpanel_create_node.md) | The parent node from which the child will be retrieved |
| index\_or\_name | [Real](../../../GML_Overview/Data_Types.md) or [String](../../../GML_Overview/Data_Types.md) | Either the index of the node or its name |

 

#### Returns:

[Flex Panel Node](flexpanel_create_node.md) or [undefined](../../../GML_Overview/Data_Types.md)

 

#### Example:
