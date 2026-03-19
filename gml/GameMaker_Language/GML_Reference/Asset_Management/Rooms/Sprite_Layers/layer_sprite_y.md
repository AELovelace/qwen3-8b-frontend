# layer\_sprite\_y

This function controls the position along the y\-axis of the room of the asset sprite element on the layer. You give the sprite element ID (which you get when you create a sprite element using [layer\_sprite\_create()](layer_sprite_create.md) or when you use the function [layer\_sprite\_get\_id()](layer_sprite_get_id.md)), and then set the y value to use (based on the room coordinates).

 

#### Syntax:

layer\_sprite\_y(sprite\_element\_id, y)

| Argument | Type | Description |
| --- | --- | --- |
| sprite\_element\_id | [Sprite Element ID](layer_sprite_get_id.md) | The unique ID value of the sprite element to change |
| y | [Real](../../../../GML_Overview/Data_Types.md) | The y position for the sprite |

 

#### Returns:

N/A

 

#### Example:

var lay\_id \= layer\_get\_id("Asset\_sky");  

 var spr\_id \= layer\_sprite\_get\_id(lay\_id, "Clouds");  

 layer\_sprite\_y(spr\_id, 50 \+ irandom(room\_height \- 200\));

The above code gets the ID value of the sprite asset "Clouds" assigned to the layer "Asset\_sky" and then sets its y position to a random value between 50 and the height of the room minus 200\.
