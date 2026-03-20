# layer\_text\_blend

This function changes the blend colour of the given Text Element, similar to [image\_blend](../../Sprites/Sprite_Instance_Variables/image_blend.md) for an Object Instance.

 

#### Syntax:

layer\_text\_blend(text\_element\_id, colour)

| Argument | Type | Description |
| --- | --- | --- |
| text\_element\_id | [Text Element ID](layer_text_get_id.md) | The text element ID, retrieved from [layer\_text\_create](layer_text_create.md) or [layer\_text\_get\_id](layer_text_get_id.md). |
| colour | [Colour](../../../Drawing/Colour_And_Alpha/Colour_And_Alpha.md) | The new blend colour of the element |

 

#### Returns:

N/A

 

#### Example:

var \_text1\_id \= layer\_text\_get\_id("Assets", "text1");  

  

 var \_text1\_blend \= layer\_text\_get\_blend(\_text1\_id);  

  

 var \_target\_colour \= keyboard\_check(vk\_space) ? c\_red : c\_white;  

  

 var \_new\_colour \= merge\_colour(\_text1\_blend, \_target\_colour, 0\.1\);  

  

 layer\_text\_blend(\_text1\_id, \_new\_colour);
 

This gets the ID of the Text Element text1 from the layer Assets, and gets its blend colour. It sets the target colour based on input, being red when space is held, and white otherwise.

It calculates a colour between the current and the target colour, moving the current colour 10% (0\.1) towards the target.

Finally it applies the new colour to the element. Each frame it moves closer to the target colour.

Since this code is for a Step event, you should initialise the \_text1\_id variable in the Create event.
