# flexpanel\_node\_get\_parent

This function returns the parent node of the given node, or [undefined](../../../GML_Overview/Data_Types.md) if it has no parent.

 

#### Syntax:

flexpanel\_node\_get\_parent(node)

| Argument | Type | Description |
| --- | --- | --- |
| node | [Flex Panel Node](flexpanel_create_node.md) | The node to get the parent of |

 

#### Returns:

[Flex Panel Node](flexpanel_create_node.md) or [undefined](../../../GML_Overview/Data_Types.md)

 

#### Example:

var \_parent \= flexpanel\_node\_get\_parent(\_node);

This gets the parent of the node \_node and stores it in a local variable.
