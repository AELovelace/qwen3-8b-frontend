# layer\_sprite\_blend

This function sets the blend colour (or "tint") of the given sprite element.

The default value is \-1 (which represents the constant c\_white, which can also be used). Any other value (including internal colour constants like c\_red, or c\_aqua) will blend the original sprite with the specified colour.

You give the sprite element ID (which you get when you create a sprite element using [layer\_sprite\_create](layer_sprite_create.md) or when you use the function [layer\_sprite\_get\_id](layer_sprite_get_id.md)), and then set the blend colour to use. Below you can see an example of a sprite that has been blended with different colours:

Please note that you should try to limit blending on the **HTML5** platform (unless using WebGL), as each blended sprite has to be cached separately and so having many blended sprites may adversely affect performance (you can also set the cache size using the function [sprite\_set\_cache\_size](../../Sprites/Sprite_Manipulation/sprite_set_cache_size.md)).

 

#### Syntax:

layer\_sprite\_blend(sprite\_element\_id, blend)

| Argument | Type | Description |
| --- | --- | --- |
| sprite\_element\_id | [Sprite Element ID](layer_sprite_get_id.md) | The unique ID value of the sprite element to change |
| blend | [Colour](../../../Drawing/Colour_And_Alpha/Colour_And_Alpha.md) | The colour to blend with the sprite (default is c\_white) |

 

#### Returns:

N/A

 

#### Example:

var \_layer\_id \= layer\_get\_id("Asset\_sky");  

 var \_sprite\_id \= layer\_sprite\_get\_id(\_layer\_id, "Clouds");  

 layer\_sprite\_blend(\_sprite\_id, c\_gray);

The above code gets the ID value of the sprite called "Clouds" assigned to the layer "Asset\_sky" and then tints it to a colour.
