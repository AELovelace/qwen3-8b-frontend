# layer\_text\_paragraphspacing

This function changes the paragraph spacing of the given Text Element.

 

#### Syntax:

layer\_text\_paragraphspacing(text\_element\_id, paragraphspacing)

| Argument | Type | Description |
| --- | --- | --- |
| text\_element\_id | [Text Element ID](layer_text_get_id.md) | The text element ID, retrieved from [layer\_text\_create](layer_text_create.md) or [layer\_text\_get\_id](layer_text_get_id.md). |
| paragraphspacing | [Real](../../../../GML_Overview/Data_Types.md) | The new paragraph spacing for the element (default is 0\). |

 

#### Returns:

N/A

 

#### Example:

var \_text1\_id \= layer\_text\_get\_id("Assets", "text1");  

  

 var \_text1\_paragraphsp \= layer\_text\_get\_paragraphspacing(\_text1\_id);  

  

 layer\_text\_paragraphspacing(\_text1\_id, \_text1\_paragraphsp \+ 4\);
 

This gets the ID of the Text Element text1 from the layer Assets, gets its paragraph spacing value and applies it back, increased by 4\.
