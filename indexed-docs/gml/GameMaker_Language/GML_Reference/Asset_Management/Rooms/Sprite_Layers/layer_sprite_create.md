# layer\_sprite\_create

With this function you can assign a sprite resource to a layer to be used in your project. You supply the layer handle (which you get when you create the layer using [layer\_create()](../General_Layer_Functions/layer_create.md) or when you use the layer name along with [layer\_get\_id()](../General_Layer_Functions/layer_get_id.md)), a position within the room, and a sprite index (which would be the name of the sprite as shown in the Asset Browser), and it will be added to the layer. The function returns the unique ID value for the element, which can then be used in further layer functions for sprites.

 

#### Syntax:

layer\_sprite\_create(layer\_id, x, y, sprite)

| Argument | Type | Description |
| --- | --- | --- |
| layer\_id | [String](../../../../GML_Overview/Data_Types.md) or [Layer](../General_Layer_Functions/layer_get_id.md) | The handle of the layer to target |
| x | [Real](../../../../GML_Overview/Data_Types.md) | The x position to use |
| y | [Real](../../../../GML_Overview/Data_Types.md) | The y position to use |
| sprite | [Sprite Asset](../../../../../The_Asset_Editors/Sprites.md) | The sprite index to be used |

 

#### Returns:

[Sprite Element ID](layer_sprite_get_id.md)

 

#### Example:

global.asset\_layer \= layer\_create(10000\);  

 for (var i \= 0; i\< 10; i\+\+)  

 {  

     var \_x \= random(room\_width);  

     var \_y \= room\_height \- 100;  

     global.asset\_spr\_trees\[i] \= layer\_sprite\_create(global.asset\_layer, \_x, \_y, spr\_Trees);  

 }

The above code creates a new layer and then adds 10 new sprite elements to it, storing the ID of each element to an array.
