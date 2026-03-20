# flexpanel\_node\_get\_struct

This function returns all the properties of the given node and its children as a struct.

This struct follows the [structure described here](../Flex_Panels_Styling.md) and can be passed into [flexpanel\_create\_node](flexpanel_create_node.md) to create a new layout tree using the same properties.

  The struct returned by this function cannot be expanded in the debugger when real\-time debugging is enabled. Its contents can be inspected, however, if you pause the game in the debugger.

 

#### Syntax:

flexpanel\_node\_get\_struct(node)

| Argument | Type | Description |
| --- | --- | --- |
| node | [Flex Panel Node](flexpanel_create_node.md) | The node to get the struct for |

 

#### Returns:

[Struct](../../../GML_Overview/Structs.md)

 

#### Example:

var \_struct \= flexpanel\_node\_get\_struct(\_node);  

 var \_new\_node \= flexpanel\_create\_node(\_struct);

This gets the struct for the node \_node and creates a new node using the same data.
