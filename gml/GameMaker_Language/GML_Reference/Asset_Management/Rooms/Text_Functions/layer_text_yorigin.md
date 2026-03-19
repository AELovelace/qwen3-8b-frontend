# layer\_text\_yorigin

This function changes the Y origin offset of the given Text Element.

This is similar to the sprite origin, and is the point within the element that acts as the "centre" for rotation. It acts as a negative offset for the text.

 

#### Syntax:

layer\_text\_yorigin(text\_element\_id, yorigin)

| Argument | Type | Description |
| --- | --- | --- |
| text\_element\_id | [Text Element ID](layer_text_get_id.md) | The text element ID, retrieved from [layer\_text\_create](layer_text_create.md) or [layer\_text\_get\_id](layer_text_get_id.md). |
| yorigin | [Real](../../../../GML_Overview/Data_Types.md) | The new Y origin of the element |

 

#### Returns:

N/A

 

#### Example:

var \_text1\_id \= layer\_text\_get\_id("Assets", "text1");  

  

 layer\_text\_x(\_text1\_id, x);  

 layer\_text\_y(\_text1\_id, y);  

  

 layer\_text\_xorigin(\_text1\_id, 0\);  

 layer\_text\_yorigin(\_text1\_id, 50\);
 

This gets the ID of the Text Element text1 from the layer Assets, and sets its position to the instance's position.

It then sets its xorigin to 0 and yorigin to 50, so it appears 50 pixels above the instance's position. This origin can later be changed to adjust the height of the text above the instance.
