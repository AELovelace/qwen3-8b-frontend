# layer\_text\_get\_paragraphspacing

This function returns the paragraph spacing (in pixels) of the given Text Element. This can be changed with [layer\_text\_paragraphspacing](layer_text_paragraphspacing.md).

 

#### Syntax:

layer\_text\_get\_paragraphspacing(text\_element\_id)

| Argument | Type | Description |
| --- | --- | --- |
| text\_element\_id | [Text Element ID](layer_text_get_id.md) | The text element ID, retrieved from [layer\_text\_create](layer_text_create.md) or [layer\_text\_get\_id](layer_text_get_id.md). |

 

#### Returns:

[Real](../../../../GML_Overview/Data_Types.md)

 

#### Example:

var \_text1\_id \= layer\_text\_get\_id("Assets", "text1");  

  

 var \_text1\_paragraphsp \= layer\_text\_get\_paragraphspacing(\_text1\_id);  

  

 layer\_text\_paragraphspacing(\_text1\_id, \_text1\_paragraphsp \+ 4\);
 

This gets the ID of the Text Element text1 from the layer Assets, gets its paragraph spacing value and applies it back, increased by 4\.
