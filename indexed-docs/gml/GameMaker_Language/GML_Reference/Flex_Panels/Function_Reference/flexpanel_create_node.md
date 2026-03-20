# flexpanel\_create\_node

This function creates a new Flex Panel node.

You can optionally pass either a JSON string or a struct containing the node's properties, which are [described here](../Flex_Panels_Styling.md). These properties can also be set later using other [Flex Panel Functions](section_index.md).

The returned node can be [inserted into another node](flexpanel_node_insert_child.md) as a child. When you no longer need a node, you must [delete it](flexpanel_delete_node.md) otherwise it will continue to stay in memory.

 

#### Syntax:

flexpanel\_create\_node(\[struct\_or\_json])

| Argument | Type | Description |
| --- | --- | --- |
| struct\_or\_json | [Struct](../../../GML_Overview/Structs.md) or [String](../../../GML_Overview/Data_Types.md) | Struct with node information or string containing JSON data, members described [on this page](../Flex_Panels_Styling.md) |

 

#### Returns:

[Flex Panel Node](flexpanel_create_node.md)

 

#### Example 1: Creating An Empty Node

n\_root \= flexpanel\_create\_node();

This creates an empty node. You can later [set properties](section_index.md) on this and [insert other nodes](flexpanel_node_insert_child.md) as children.

 

#### Example 2: Passing a Struct

 
This creates a node using a struct. That struct contains information on the properties of the root node and all of its nested children, which is copied to create the [Flex Panel Node](flexpanel_create_node.md) struct.

 

#### Example 3: Passing a JSON String

n\_root \= flexpanel\_create\_node(@'{  

     "width": "80%", "height": 200, "padding": 20,  

     "nodes": \[  

         {  

             "height": 20  

         },  

         {  

             "flex": 1, "flexDirection": "row",  

             "nodes": \[  

                 { "aspectRatio": 1 },  

                 { "aspectRatio": 1 },  

                 { "aspectRatio": 1 },  

             ]  

         },  

         {  

             "height": 20  

         },  

     ]  

 }');

This creates the same nodes as before, however this uses a JSON [multi\-line string](../../Strings/Strings.md#@) instead of a struct.
