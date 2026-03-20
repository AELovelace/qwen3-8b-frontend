# layer\_text\_linespacing

This function changes the line spacing of the given Text Element. This is the space (in pixels) added between each line in the displayed string.

 

#### Syntax:

layer\_text\_linespacing(text\_element\_id, linespacing)

| Argument | Type | Description |
| --- | --- | --- |
| text\_element\_id | [Text Element ID](layer_text_get_id.md) | The text element ID, retrieved from [layer\_text\_create](layer_text_create.md) or [layer\_text\_get\_id](layer_text_get_id.md). |
| linespacing | [Real](../../../../GML_Overview/Data_Types.md) | The new line spacing for the element. |

 

#### Returns:

N/A

 

#### Example:

var \_text1\_id \= layer\_text\_get\_id("Assets", "text1");  

  

 var \_text1\_linesp \= layer\_text\_get\_linespacing(\_text1\_id);  

  

 layer\_text\_linespacing(\_text1\_id, \_text1\_linesp \+ 4\);
 

This gets the ID of the Text Element text1 from the layer Assets, gets its line spacing value and applies it back, increased by 4\.
