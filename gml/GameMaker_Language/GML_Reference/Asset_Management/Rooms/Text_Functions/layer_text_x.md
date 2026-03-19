# layer\_text\_x

This function changes the X (horizontal) position of the given Text Element. Note that the text's X position will be offset by the element's [xorigin](layer_text_xorigin.md) value.

 

#### Syntax:

layer\_text\_x(text\_element\_id, x)

| Argument | Type | Description |
| --- | --- | --- |
| text\_element\_id | [Text Element ID](layer_text_get_id.md) | The text element ID, retrieved from [layer\_text\_create](layer_text_create.md) or [layer\_text\_get\_id](layer_text_get_id.md). |
| x | [Real](../../../../GML_Overview/Data_Types.md) | The X position of the element |

 

#### Returns:

N/A

 

#### Example:

var \_text1\_id \= layer\_text\_get\_id("Assets", "text1");  

  

 var \_text1\_pos \=  

 {  

     x : layer\_text\_get\_x(\_text1\_id),  

     y : layer\_text\_get\_y(\_text1\_id)  

 }  

  

 if (\_text1\_pos.y \> room\_height) \_text1\_pos.y \= 0;  

 if (\_text1\_pos.y \< 0\) \_text1\_pos.y \= room\_height;  

 if (\_text1\_pos.x \> room\_width) \_text1\_pos.x \= 0;  

 if (\_text1\_pos.x \< 0\) \_text1\_pos.x \= room\_width;  

  

 layer\_text\_x(\_text1\_id, \_text1\_pos.x \+ 4\);  

 layer\_text\_y(\_text1\_id, \_text1\_pos.y \+ 4\);
 

This gets the ID of the Text Element text1 from the layer Assets, and then gets its X and Y positions, storing them into a struct.

It then performs a check on those coordinates, and if they reach one end of the room, they are set to the other end (e.g. going through the right boundary puts you at the left boundary, and so on).

Finally, it applies the positions back to the element, with 4 added to each component so it shifts its position every frame, moving down and right by 4 pixels each.

Since this code is for a Step event, you should initialise the \_text1\_id variable in the Create event.
