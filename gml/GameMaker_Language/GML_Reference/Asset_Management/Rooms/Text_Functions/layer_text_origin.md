# layer\_text\_origin

This function changes the frame origin of the given Text Element. This controls how the text frame is aligned relative to the position of the element.

You can supply any one of the following constants:

 
 

#### Syntax:

layer\_text\_origin(text\_element\_id, origin)

| Argument | Type | Description |
| --- | --- | --- |
| text\_element\_id | [Text Element ID](layer_text_get_id.md) | The text element ID, retrieved from [layer\_text\_create](layer_text_create.md) or [layer\_text\_get\_id](layer_text_get_id.md). |
| origin | [Text Frame Origin Constant](layer_text_origin.md) | The origin to apply |

 

#### Returns:

N/A

 

#### Example:

var \_text1\_id \= layer\_text\_get\_id("Assets", "text1");  

  

 layer\_text\_origin(\_text1\_id, origin\_bottomcentre).
 

This gets the ID of the Text Element text1 from the layer Assets, and sets its frame origin to bottom\-centre.
