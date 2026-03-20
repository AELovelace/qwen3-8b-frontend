# layer\_sprite\_get\_yscale

This function can be used to get the current scale multiplier along the y axis for the sprite element. You give the sprite element ID (which you get when you create a sprite element using [layer\_sprite\_create()](layer_sprite_create.md) or when you use the function [layer\_sprite\_get\_id()](layer_sprite_get_id.md)), and the function will return real value for the y scale, where 1 is no scaling.

 

#### Syntax:

layer\_sprite\_get\_yscale(sprite\_element\_id)

| Argument | Type | Description |
| --- | --- | --- |
| sprite\_element\_id | [Sprite Element ID](layer_sprite_get_id.md) | The unique ID value of the sprite element to get the information from |

 

#### Returns:

[Real](../../../../GML_Overview/Data_Types.md)

 

#### Example:

var lay\_id \= layer\_get\_id("sprite\_sky");  

 var spr\_id \= layer\_sprite\_get\_id(lay\_id, "Clouds");  

 if (layer\_sprite\_get\_yscale(spr\_id) !\= 1\)  

 {  

     layer\_sprite\_yscale(spr\_id, 1\);  

 }

The above code will get the layer handle for the layer named "sprite\_sky" and then use that to get the ID of the sprite element on that layer. This ID is then used to check the yscale value and if it is anything other than 1 it is set to 1\.
