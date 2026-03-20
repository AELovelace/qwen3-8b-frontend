# layer\_text\_wrap

This function enables or disables wrapping of text in the given Text Element. When enabled, text is moved to the next line when the current line width exceeds the [frame width](layer_text_framew.md).

 

#### Syntax:

layer\_text\_wrap(text\_element\_id, wrap)

| Argument | Type | Description |
| --- | --- | --- |
| text\_element\_id | [Text Element ID](layer_text_get_id.md) | The text element ID, retrieved from [layer\_text\_create](layer_text_create.md) or [layer\_text\_get\_id](layer_text_get_id.md). |
| wrap | [Boolean](../../../../GML_Overview/Data_Types.md) | Enable (true) or disable (false) wrapping |

 

#### Returns:

N/A

 

#### Example:

var \_text1\_id \= layer\_text\_get\_id("Assets", "text1");  

  

 var \_text1\_wrap \= layer\_text\_get\_wrap(\_text1\_id);  

  

 layer\_text\_wrap(\_text1\_id, !\_text1\_wrap);
 

This gets the ID of the Text Element text1 from the layer Assets, and gets the wrapping boolean value. It then reapplies the boolean value after flipping it, so if wrapping is disabled, it will be enabled, and vice versa.
