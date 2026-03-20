# layer\_text\_charspacing

This function changes the character spacing of the given Text Element. This is the space (in pixels) added between each character in the displayed string.

 

#### Syntax:

layer\_text\_charspacing(text\_element\_id, charspacing)

| Argument | Type | Description |
| --- | --- | --- |
| text\_element\_id | [Text Element ID](layer_text_get_id.md) | The text element ID, retrieved from [layer\_text\_create](layer_text_create.md) or [layer\_text\_get\_id](layer_text_get_id.md). |
| charspacing | [Real](../../../../GML_Overview/Data_Types.md) | The new character spacing for the element. |

 

#### Returns:

N/A

 

#### Example:

var \_text1\_id \= layer\_text\_get\_id("Assets", "text1");  

  

 var \_text1\_charsp \= layer\_text\_get\_charspacing(\_text1\_id);  

  

 layer\_text\_charspacing(\_text1\_id, \_text1\_charsp \+ 2\);
 

This gets the ID of the Text Element text1 from the layer Assets, gets its character spacing value and applies it back, increased by 2\.
