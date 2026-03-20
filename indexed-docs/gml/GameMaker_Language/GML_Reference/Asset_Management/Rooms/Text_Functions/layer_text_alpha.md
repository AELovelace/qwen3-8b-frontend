# layer\_text\_alpha

This function changes the alpha (opacity) of the given Text Element. This is a value between 0 (invisible) and 1 (fully visible).

 

#### Syntax:

layer\_text\_alpha(text\_element\_id, alpha)

| Argument | Type | Description |
| --- | --- | --- |
| text\_element\_id | [Text Element ID](layer_text_get_id.md) | The text element ID, retrieved from [layer\_text\_create](layer_text_create.md) or [layer\_text\_get\_id](layer_text_get_id.md). |
| alpha | [Real](../../../../GML_Overview/Data_Types.md) | The new alpha of the element |

 

#### Returns:

N/A

 

#### Example:

var \_text1\_id \= layer\_text\_get\_id("Assets", "text1");  

  

 var \_text1\_alpha \= layer\_text\_get\_alpha(\_text1\_id);  

  

 var \_target\_alpha \= keyboard\_check(vk\_space) ? 1 : 0;  

  

 var \_new\_alpha \= lerp(\_text1\_alpha, \_target\_alpha, 0\.1\);  

  

 layer\_text\_alpha(\_text1\_id, \_new\_alpha);
 

This gets the ID of the Text Element text1 from the layer Assets, and gets its alpha. It sets the target alpha based on input, being 1 (visible) when space is held, and 0 (invisible) otherwise.

It calculates a value between the current and the target alpha, moving the current alpha 10% (0\.1) towards the target.

Finally it applies the new alpha to the element. Each frame it moves closer to the target alpha.

Since this code is for a Step event, you should initialise the \_text1\_id variable in the Create event.
