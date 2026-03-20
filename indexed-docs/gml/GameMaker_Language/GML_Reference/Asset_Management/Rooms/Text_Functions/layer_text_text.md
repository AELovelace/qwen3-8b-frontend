# layer\_text\_text

This function changes the text of the given Text Element. You supply the Text Element to modify, and the string that should appear on that element.

 

#### Syntax:

layer\_text\_text(text\_element\_id, text)

| Argument | Type | Description |
| --- | --- | --- |
| text\_element\_id | [Text Element ID](layer_text_get_id.md) | The text element ID, retrieved from [layer\_text\_create](layer_text_create.md) or [layer\_text\_get\_id](layer_text_get_id.md). |
| text | [String](../../../../GML_Overview/Data_Types.md) | The text string that appears on the element. |

 

#### Returns:

N/A

 

#### Example:

var \_number \= 5;  

  

 var \_text1\_id \= layer\_text\_get\_id("Assets", "text1");  

  

 var \_text1\_text \= layer\_text\_get\_text(\_text1\_id);  

  

 layer\_text\_text(\_text1\_id, $"{\_text1\_text} ({\_number})");
 

This gets the ID of the Text Element text1 from the layer Assets, and retrieves its text string. It then reapplies the text string back to the element, but with a number value added to it, inside parentheses. For example, if the text was "Waiting for players" it will become "Waiting for players (5\)".
