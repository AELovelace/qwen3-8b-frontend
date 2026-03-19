# layer\_text\_wrapmode

This function changes the wrap mode of the given Text Element. In the IDE this is present as the "Split words" option.

You can supply any one of the following constants:

 
 
 

#### Syntax:

layer\_text\_wrapmode(text\_element\_id, wrapmode)

| Argument | Type | Description |
| --- | --- | --- |
| text\_element\_id | [Text Element ID](layer_text_get_id.md) | The text element ID, retrieved from [layer\_text\_create](layer_text_create.md) or [layer\_text\_get\_id](layer_text_get_id.md). |
| wrapmode | [Text Wrap Mode Constant](layer_text_wrapmode.md) | The wrap mode to use |

 

#### Returns:

N/A

 

#### Example:

var \_text1\_id \= layer\_text\_get\_id("Assets", "text1");  

  

 layer\_text\_wrapmode(\_text1\_id, textwrap\_splitwords);
 

This gets the ID of the Text Element text1 from the layer Assets, and sets its wrap mode to "Split words".
