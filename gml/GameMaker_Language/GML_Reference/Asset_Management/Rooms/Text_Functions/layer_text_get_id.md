# layer\_text\_get\_id

This function returns the ID of a Text Element which was placed in the Room Editor. This ID can be used in the [Text Element Functions](Text_Elements.md).

You must provide a layer to check in (UI layers are also accepted), and the name of the text element as set in the Room Editor, as a string:

#### Syntax:

layer\_text\_get\_id(layer\_name\_or\_id, text\_element\_name)

| Argument | Type | Description |
| --- | --- | --- |
| layer\_name\_or\_id | [String](../../../../GML_Overview/Data_Types.md) or [Layer](../General_Layer_Functions/layer_get_id.md) | The layer to check. |
| text\_element\_name | [String](../../../../GML_Overview/Data_Types.md) | The name of the Text Element as a string, see image above. |

 

#### Returns:

[Text Element ID](layer_text_get_id.md)

 

#### Example:

var \_text1\_id \= layer\_text\_get\_id("Assets", "text1");  

  

 if (layer\_text\_exists("Assets", \_text1\_id))  

 {  

     layer\_text\_destroy(\_text1\_id);  

 }
 

This gets the ID of the Text Element text1 from the Assets layer. It then checks whether that element exists, and if it does, it destroys it.
