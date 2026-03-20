# flexpanel\_node\_get\_measure\_function

This function returns the [Measure Function](flexpanel_node_set_measure_function.md) set for the given [Flex Panel Node](flexpanel_create_node.md). If none is set, it will return [undefined](../../../GML_Overview/Data_Types.md).

 

#### Syntax:

flexpanel\_node\_get\_measure\_function(node)

| Argument | Type | Description |
| --- | --- | --- |
| node | [Flex Panel Node](flexpanel_create_node.md) | The node to check |

 

#### Returns:

[Function](../../../GML_Overview/Script_Functions.md) or [undefined](../../../GML_Overview/Data_Types.md)

 

#### Example:

var \_measure\_func \= flexpanel\_node\_get\_measure\_function(\_node);  

  

 if (\_measure\_func \=\= undefined)  

 {  

     flexpanel\_node\_set\_measure\_function(\_node, text\_measure\_function);  

 }
 

This gets the measure function of the node \_node and stores it in a local variable. If it's undefined, it applies an existing [Method](../../../GML_Overview/Method_Variables.md) to the node as the measure function.
