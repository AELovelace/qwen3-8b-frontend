# layer\_get\_flexpanel\_node

This function takes a [Layer](../General_Layer_Functions/layer_get_id.md) handle or the name of a layer as a string. If the layer is a [UI layer](../../../../../The_Asset_Editors/Room_Properties/UI_Layers.md), it will return the [Flex Panel Node](../../../Flex_Panels/Function_Reference/flexpanel_create_node.md) for the root of the UI layer, otherwise it will return undefined.

  Use [flexpanel\_node\_get\_struct](../../../Flex_Panels/Function_Reference/flexpanel_node_get_struct.md) to return the struct for a node. The contents of the returned struct are defined here: [Flex Panel Struct Members](../../../Flex_Panels/Flex_Panels_Styling.md)

 

#### Syntax:

layer\_get\_flexpanel\_node(layer\_id\_or\_name)

| Argument | Type | Description |
| --- | --- | --- |
| layer\_id\_or\_name | [Layer](../General_Layer_Functions/layer_get_id.md) or [String](../../../../GML_Overview/Data_Types.md) | The layer to get the Flex Panel Node for |

 

#### Returns:

[Flex Panel Node](../../../Flex_Panels/Function_Reference/flexpanel_create_node.md) or undefined

 

#### Example:

var \_ui\_layer \= layer\_get\_flexpanel\_node("UILayer\_1");  

  

 var \_hearts\_flex \= flexpanel\_node\_get\_child(\_ui\_layer, "Hearts");  

  

 flexpanel\_node\_style\_set\_width(\_hearts\_flex, 200, flexpanel\_unit.point);
 

This gets the [Flex Panel Node](../../../Flex_Panels/Function_Reference/flexpanel_create_node.md) of a UI layer and retrieves a child panel called "**Hearts**". It sets the width of that panel to 200px.
