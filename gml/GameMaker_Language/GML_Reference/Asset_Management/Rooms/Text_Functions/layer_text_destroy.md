# layer\_text\_destroy

This function destroys the given Text Element.

 

#### Syntax:

layer\_text\_destroy(text\_element\_id)

| Argument | Type | Description |
| --- | --- | --- |
| text\_element\_id | [Text Element ID](layer_text_get_id.md) | The text element ID, retrieved from [layer\_text\_create](layer_text_create.md) or [layer\_text\_get\_id](layer_text_get_id.md). |

 

#### Returns:

N/A

 

#### Example:

var \_text1\_id \= layer\_text\_get\_id("Assets", "text1");  

  

 if (layer\_text\_exists("Assets", \_text1\_id))  

 {  

     layer\_text\_destroy(\_text1\_id);  

 }
 

This gets the ID of the Text Element text1 from the Assets layer. It then checks whether that element exists, and if it does, it destroys it.
