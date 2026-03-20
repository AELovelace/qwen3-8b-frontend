# layer\_sprite\_yscale

Using this function you can change whether the given sprite element on a layer should be scaled along the y axis or not. You give the sprite element ID (which you get when you create a sprite element using [layer\_sprite\_create()](layer_sprite_create.md) or when you use the function [layer\_sprite\_get\_id()](layer_sprite_get_id.md)), and then set the scale value. A scale of 1 indicates no scaling (1:1\), smaller values will scale down (0\.5, for example, will half the height of the sprite used), larger values will scale up, and negative values will mirror the sprite and scale it unless the value used is exactly \-1 (in which case the sprite used is just mirrored top\-to\-bottom about its (0, 0\) position with no scaling).

 

#### Syntax:

layer\_sprite\_yscale(sprite\_element\_id, yscale)

| Argument | Type | Description |
| --- | --- | --- |
| sprite\_element\_id | [Sprite Element ID](layer_sprite_get_id.md) | The unique ID value of the sprite element to change |
| yscale | [Real](../../../../GML_Overview/Data_Types.md) | The yscale value (default is 1\) |

 

#### Returns:

N/A

 

#### Example:

var asset\_sprite \= layer\_sprite\_get\_id(layer, "gfc\_Trees");  

 if layer\_sprite\_get\_xscale(asset\_sprite) !\= 1 \|\| layer\_sprite\_get\_yscale(asset\_sprite) !\= 1  

 {  

     layer\_sprite\_xscale(asset\_sprite, 1\);  

     layer\_sprite\_yscale(asset\_sprite, 1\);  

 }

The above code will check the sprite element assigned to the layer the instance running the code is on and if it is scaled in either direction it will set both the x\-axis scale and y\-axis scale to 1\.
