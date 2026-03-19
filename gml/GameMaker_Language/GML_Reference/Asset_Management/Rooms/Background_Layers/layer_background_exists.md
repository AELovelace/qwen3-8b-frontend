# layer\_background\_exists

You can use this function to check and see if a background element exists on any given layer. You supply the layer handle (which you get when you create the layer using [layer\_create()](../General_Layer_Functions/layer_create.md)) or the layer name (as a string \- this will have a performance impact) and the background element ID (which you get when you create a background element using [layer\_background\_create()](layer_background_create.md) or when you use the function [layer\_background\_get\_id()](layer_background_get_id.md)) and the function will return either true if the element exists, or false if it does not.

 This function works within the scope of the current target room \- by default the room in which the function is called \- which can be set using the function [layer\_set\_target\_room()](../General_Layer_Functions/layer_set_target_room.md).

 

#### Syntax:

layer\_background\_exists(layer\_id, background\_element\_id)

| Argument | Type | Description |
| --- | --- | --- |
| layer\_id | [String](../../../../GML_Overview/Data_Types.md) or [Layer](../General_Layer_Functions/layer_get_id.md) | The handle of the layer to target (or the layer name as a string) |
| background\_element\_id | [Background Element ID](layer_background_get_id.md) | The unique ID value of the background element to check |

 

#### Returns:

[Boolean](../../../../GML_Overview/Data_Types.md)

 

#### Example:

var lay\_id \= layer\_get\_id("Background\_trees");  

 if (layer\_background\_exists(lay\_id, global.TreesBackground))  

  

 {  

     layer\_background\_destroy(lay\_id, global.TreesBackground);  

 }
 

The above code checks the layer "Background\_trees" to see if the given background element exists and if it does, then it is destroyed (but not the layer).
