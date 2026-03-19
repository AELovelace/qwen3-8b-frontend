# layer\_text\_get\_halign

This function returns the horizontal alignment mode of the given Text Element. This can be changed with [layer\_text\_halign](layer_text_halign.md).

This will return one of the following constants:

 
 

#### Syntax:

layer\_text\_get\_halign(text\_element\_id)

| Argument | Type | Description |
| --- | --- | --- |
| text\_element\_id | [Text Element ID](layer_text_get_id.md) | The text element ID, retrieved from [layer\_text\_create](layer_text_create.md) or [layer\_text\_get\_id](layer_text_get_id.md). |

 

#### Returns:

[Text Horizontal Alignment Constant](layer_text_halign.md)

 

#### Example:

var \_text1\_id \= layer\_text\_get\_id("Assets", "text1");  

  

 text1\_old\_halign \= layer\_text\_get\_halign(\_text1\_id);  

 text1\_old\_valign \= layer\_text\_get\_valign(\_text1\_id);  

  

 layer\_text\_halign(\_text1\_id, textalign\_center);  

 layer\_text\_valign(\_text1\_id, textalign\_bottom);
 

This gets the ID of the Text Element text1 from the layer Assets, and stores its horizontal and vertical alignments into variables, before changing the alignments. These variables can later be used to reset the alignment values to what they were before they were changed here.
