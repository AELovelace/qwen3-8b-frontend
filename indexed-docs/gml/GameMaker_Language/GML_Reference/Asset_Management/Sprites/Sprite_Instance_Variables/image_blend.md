# image\_blend

This variable controls the "tinting" of the instance sprite and the default value is \-1 (but can also be c\_white). Any other value (including internal colour constants like c\_red, or c\_aqua) will blend the specified colour with the original sprite. Please note that for changes in this variable to be visible, the instance should have either *no* draw event (and so GameMaker will default draw the sprite) or be drawn using one of the extended drawing functions like [draw\_self()](../../../Drawing/Sprites_And_Tiles/draw_self.md) or [draw\_sprite\_ext()](../../../Drawing/Sprites_And_Tiles/draw_sprite_ext.md).

Please note that you should try to limit blending on the HTML5 platform (unless using WebGL), as each blended sprite has to be cached separately and so having many blended sprites may adversely affect performance (you can also set the cache size using the function [sprite\_set\_cache\_size()](../Sprite_Manipulation/sprite_set_cache_size.md)).

 

#### Syntax:

image\_blend

 

#### Returns:

Colour Constant

 

#### Example:

image\_blend \= make\_colour\_hsv(255, 255, random(255\));

The above code will set the image\_blend of the sprite defined for the instance to a random colour.
