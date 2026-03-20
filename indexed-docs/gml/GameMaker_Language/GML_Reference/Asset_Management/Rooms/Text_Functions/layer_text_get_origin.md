# layer\_text\_get\_origin

This function returns the frame origin of the given Text Element. It will return one of the following constants:

 
 

#### Syntax:

layer\_text\_get\_origin(text\_element\_id)

| Argument | Type | Description |
| --- | --- | --- |
| text\_element\_id | [Text Element ID](layer_text_get_id.md) | The text element ID, retrieved from [layer\_text\_create](layer_text_create.md) or [layer\_text\_get\_id](layer_text_get_id.md). |

 

#### Returns:

[Text Frame Origin Constant](layer_text_origin.md)

 

#### Example:

var \_text1\_id \= layer\_text\_get\_id("Assets", "text1");  

  

 var \_text1\_forigin \= layer\_text\_get\_origin(\_text1\_id);
 

This gets the ID of the Text Element text1 from the layer Assets, and stores its frame origin value in a new local variable.
