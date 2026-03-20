# flexpanel\_node\_set\_measure\_function

This function sets the [Measure Function](https://www.yogalayout.dev/docs/advanced/external-layout-systems) of the given [Flex Panel Node](flexpanel_create_node.md) (must be a leaf node, i.e. a node that has no children).

The Measure Function for a leaf node is run when its layout is calculated and a measurement for the node is needed, which may not always be required (i.e. in case it already has a size defined).

The provided function will receive four arguments: (width, width\_type, height, height\_type). The (width/height)\_type arguments can be one of the following values:

- **0**: Undefined
- **1**: Exactly
- **2**: At Most

The Measure Function must return a struct with width and height variables (or at least one of them). These will be the dimensions applied to the node.

For information on Measure Functions, see [Integrating with external layout systems](https://www.yogalayout.dev/docs/advanced/external-layout-systems).

 

#### Syntax:

flexpanel\_node\_set\_measure\_function(node, function)

| Argument | Type | Description |
| --- | --- | --- |
| node | [Flex Panel Node](flexpanel_create_node.md) | The node to modify |
| function | [Function](../../../GML_Overview/Script_Functions.md) | The Measure Function to use, or [undefined](../../../GML_Overview/Data_Types.md) to reset to the default behaviour |

 

#### Returns:

N/A

 

#### Example:

var \_measure\_func \= flexpanel\_node\_get\_measure\_function(\_node);  

  

 if (\_measure\_func \=\= undefined)  

 {  

     var \_text\_measure\_function \= function(\_width, \_width\_type, \_height, \_height\_type)  

     {  

         show\_debug\_message( $"width\={\_width}, height\={\_height}, width\_type\={\_width\_type}, height\_type\={\_height\_type}" );  

         return { width : \_width/2, height : \_height/2 };  

     };  

  

     flexpanel\_node\_set\_measure\_function(\_node, \_text\_measure\_function);  

 }
 

This gets the measure function of the node \_node and stores it in a local variable. If it's undefined, it creates a [Method](../../../GML_Overview/Method_Variables.md) and applies that to the node as the measure function. The method, when run, outputs the values of the arguments to the Output Log and returns a struct with the width and height halved.
