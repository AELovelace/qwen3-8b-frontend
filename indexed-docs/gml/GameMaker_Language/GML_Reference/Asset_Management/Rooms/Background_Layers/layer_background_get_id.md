# layer\_background\_get\_id

This function can be used to retrieve the unique ID value of the background element on a layer. You supply the layer handle (which you get when you use the layer name along with [layer\_get\_id()](../General_Layer_Functions/layer_get_id.md)) and the function will return the ID value associated with the background element on the layer.

For layers created at runtime, this will return the first background element assigned to that layer.

 

#### Syntax:

layer\_background\_get\_id(layer\_id)

| Argument | Type | Description |
| --- | --- | --- |
| layer\_id | [String](../../../../GML_Overview/Data_Types.md) or [Layer](../General_Layer_Functions/layer_get_id.md) | The handle of the layer to target |

 

#### Returns:

[Background Element ID](layer_background_get_id.md)

 

#### Example:

var lay\_id \= layer\_get\_id("Background\_trees");  

 var back\_id \= layer\_background\_get\_id(lay\_id);  

 layer\_background\_sprite(back\_id, bck\_Trees\_Winter);

The above code will get the layer handle for the layer named "Background\_trees" and then use that to get the ID of the background element on that layer. This ID is then used to change the element sprite.
