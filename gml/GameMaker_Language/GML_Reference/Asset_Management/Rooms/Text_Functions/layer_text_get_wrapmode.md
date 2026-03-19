# layer\_text\_get\_wrapmode

This function returns the wrap mode of the given Text Element. It will return one of the following constants:

 
 

#### Syntax:

layer\_text\_get\_wrapmode(text\_element\_id)

| Argument | Type | Description |
| --- | --- | --- |
| text\_element\_id | [Text Element ID](layer_text_get_id.md) | The text element ID, retrieved from [layer\_text\_create](layer_text_create.md) or [layer\_text\_get\_id](layer_text_get_id.md). |

 

#### Returns:

[Text Wrap Mode Constant](layer_text_wrapmode.md)

 

#### Example:

var \_text1\_id \= layer\_text\_get\_id("Assets", "text1");  

  

 var \_text1\_wrapmode \= layer\_text\_get\_wrapmode(\_text1\_id);
 

This gets the ID of the Text Element text1 from the layer Assets, and stores its wrap mode in a new local variable.
