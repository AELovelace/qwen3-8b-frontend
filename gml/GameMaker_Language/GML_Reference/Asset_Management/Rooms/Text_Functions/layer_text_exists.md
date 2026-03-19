# layer\_text\_exists

This function checks whether the given Text Element exists on the given layer, and returns true or false.

 

#### Syntax:

layer\_text\_exists(layer\_name\_or\_id, text\_element\_id)

| Argument | Type | Description |
| --- | --- | --- |
| layer\_name\_or\_id | [String](../../../../GML_Overview/Data_Types.md) or [Layer](../General_Layer_Functions/layer_get_id.md) | The layer to check. |
| text\_element\_id | [Text Element ID](layer_text_get_id.md) | The text element ID, retrieved from [layer\_text\_create](layer_text_create.md) or [layer\_text\_get\_id](layer_text_get_id.md). |

 

#### Returns:

[Boolean](../../../../GML_Overview/Data_Types.md)

 

#### Example:

var \_text1\_id \= layer\_text\_get\_id("Assets", "text1");  

  

 if (layer\_text\_exists("Assets", \_text1\_id))  

 {  

     layer\_text\_destroy(\_text1\_id);  

 }
 

This gets the ID of the Text Element text1 from the Assets layer. It then checks whether that element exists, and if it does, it destroys it.
