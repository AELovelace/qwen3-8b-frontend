# layer\_text\_get\_linespacing

This function returns the line spacing (in pixels) of the given Text Element. This can be changed with [layer\_text\_linespacing](layer_text_linespacing.md).

 

#### Syntax:

layer\_text\_get\_linespacing(text\_element\_id)

| Argument | Type | Description |
| --- | --- | --- |
| text\_element\_id | [Text Element ID](layer_text_get_id.md) | The text element ID, retrieved from [layer\_text\_create](layer_text_create.md) or [layer\_text\_get\_id](layer_text_get_id.md). |

 

#### Returns:

[Real](../../../../GML_Overview/Data_Types.md)

 

#### Example:

var \_text1\_id \= layer\_text\_get\_id("Assets", "text1");  

  

 var \_text1\_linesp \= layer\_text\_get\_linespacing(\_text1\_id);  

  

 layer\_text\_linespacing(\_text1\_id, \_text1\_linesp \+ 4\);
 

This gets the ID of the Text Element text1 from the layer Assets, gets its line spacing value and applies it back, increased by 4\.
