# layer\_text\_frameh

This function changes the frame height of the given Text Element.

 

#### Syntax:

layer\_text\_frameh(text\_element\_id, height)

| Argument | Type | Description |
| --- | --- | --- |
| text\_element\_id | [Text Element ID](layer_text_get_id.md) | The text element ID, retrieved from [layer\_text\_create](layer_text_create.md) or [layer\_text\_get\_id](layer_text_get_id.md). |
| height | [Real](../../../../GML_Overview/Data_Types.md) | The new frame height of the element. |

 

#### Returns:

N/A

 

#### Example:

var \_text1\_id \= layer\_text\_get\_id("Assets", "text1");  

  

 layer\_text\_framew(\_text1\_id, room\_width \* 0\.5\);  

 layer\_text\_frameh(\_text1\_id, 64\);
 

This gets the ID of the Text Element text1 from the layer Assets, then sets its frame width to half the room's size, and the frame height to 64\.
