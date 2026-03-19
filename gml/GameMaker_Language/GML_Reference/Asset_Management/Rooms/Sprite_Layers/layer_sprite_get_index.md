# layer\_sprite\_get\_index

This function can be used to get the current image index value of the sprite element. You give the sprite element ID (which you get when you create a sprite element using [layer\_sprite\_create()](layer_sprite_create.md) or when you use the function [layer\_sprite\_get\_id()](layer_sprite_get_id.md)), and the function will return real value that represents the image index being shown for the sprite. The function will return \-1 if either the sprite element doesn't exist or the element doesn't have a valid sprite assigned to it.

 

#### Syntax:

layer\_sprite\_get\_index(sprite\_element\_id)

| Argument | Type | Description |
| --- | --- | --- |
| sprite\_element\_id | [Sprite Element ID](layer_sprite_get_id.md) | The unique ID value of the sprite element to get the information from |

 

#### Returns:

[Real](../../../../GML_Overview/Data_Types.md) or \-1

 

#### Example:

var lay\_id \= layer\_get\_id("sprite\_sky");  

 var spr\_id \= layer\_sprite\_get\_id(lay\_id, "Clouds");  

 if (layer\_sprite\_get\_index(spr\_id) \< 4\)  

 {  

     layer\_sprite\_index(spr\_id, 4\);  

 }

The above code will get the layer handle for the layer named "sprite\_sky" and then use that to get the ID of the sprite element on that layer. This ID is then used to check if the image index for the element is less than 4, and if so it is set to 4\.
