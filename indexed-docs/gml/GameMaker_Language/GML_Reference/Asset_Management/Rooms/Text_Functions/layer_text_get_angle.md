# layer\_text\_get\_angle

This function returns the angle (rotation value) of the given Text Element. This can be changed with [layer\_text\_angle](layer_text_angle.md).

 

#### Syntax:

layer\_text\_get\_angle(text\_element\_id)

| Argument | Type | Description |
| --- | --- | --- |
| text\_element\_id | [Text Element ID](layer_text_get_id.md) | The text element ID, retrieved from [layer\_text\_create](layer_text_create.md) or [layer\_text\_get\_id](layer_text_get_id.md). |

 

#### Returns:

[Real](../../../../GML_Overview/Data_Types.md)

 

#### Example:

var \_text1\_id \= layer\_text\_get\_id("Assets", "text1");  

  

 var \_text1\_angle \= layer\_text\_get\_angle(\_text1\_id);  

  

 layer\_text\_angle(\_text1\_id, \_text1\_angle \+ 5\);
 

This gets the ID of the Text Element text1 from the layer Assets, and then gets its angle. It applies the angle back with 5 added to it, so the element rotates 5 degrees every frame.

Since this code is for a Step event, you should initialise the \_text1\_id variable in the Create event.
