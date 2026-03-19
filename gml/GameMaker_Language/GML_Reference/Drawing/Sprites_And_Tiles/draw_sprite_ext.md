# draw\_sprite\_ext

This function will draw the given sprite as in the function [draw\_sprite](draw_sprite.md) but with additional options to change the scale, blending, rotation and alpha of the sprite being drawn. Changing these values does *not* modify the resource in any way (only how it is drawn), and you can use any of the available [Sprite Instance Variables](../../Asset_Management/Sprites/Sprite_Instance_Variables/Sprite_Instance_Variables.md) instead of direct values for all arguments in the function. The image below illustrates how different values affect the drawing of the sprite:

 

  Colour blending is only recommended for the HTML5 target when WebGL is enabled, although you can still set the blending colour if it is not enabled and it will blend the sprite as normal. However, all blending done in this way creates a duplicate sprite which is then stored in the cache and used when required. This is far from optimal and if you use multiple colour changes it will slow down your game's performance unless you activate WebGL. If you do not wish to use WebGL, then you can set the cache size to try and limit this should it be necessary using the function [sprite\_set\_cache\_size](../../Asset_Management/Sprites/Sprite_Manipulation/sprite_set_cache_size.md).

  This function may not work as expected when using skeleton animation sprites, and you may find that the function only draws the first frame of the default pose. You should be using the draw\_skeleton\_\* functions instead.

 

#### Syntax:

draw\_sprite\_ext( sprite, subimg, x, y, xscale, yscale, rot, colour, alpha)

| Argument | Type | Description |
| --- | --- | --- |
| sprite | [Sprite Asset](../../../../The_Asset_Editors/Sprites.md) | The sprite to draw. |
| subimg | [Real](../../../GML_Overview/Data_Types.md) | The sub\-image (frame) of the sprite to draw ([image\_index](../../Asset_Management/Sprites/Sprite_Instance_Variables/image_index.md) or \-1 correlate to the current frame of animation in the object). |
| x | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate of where to draw the sprite. |
| y | [Real](../../../GML_Overview/Data_Types.md) | The y coordinate of where to draw the sprite. |
| xscale | [Real](../../../GML_Overview/Data_Types.md) | The horizontal scaling of the sprite, as a multiplier: 1 \= normal scaling, 0\.5 is half, etc. |
| yscale | [Real](../../../GML_Overview/Data_Types.md) | The vertical scaling of the sprite as a multiplier: 1 \= normal scaling, 0\.5 is half, etc. |
| rot | [Real](../../../GML_Overview/Data_Types.md) | The rotation of the sprite. 0\=right way up, 90\=rotated 90 degrees counter\-clockwise, etc. |
| colour | [Colour](../Colour_And_Alpha/Colour_And_Alpha.md) | The colour with which to blend the sprite. c\_white is to display it normally. |
| alpha | [Real](../../../GML_Overview/Data_Types.md) | The alpha of the sprite (from 0 to 1 where 0 is transparent and 1 opaque). |

 

#### Returns:

N/A

 

#### Example:

draw\_sprite\_ext(sprite\_index, image\_index, x, y, image\_xscale, image\_yscale, image\_angle, image\_blend, image\_alpha);

This will draw the instance's assigned sprite using its default values (essentially the same as using [draw\_self](draw_self.md)).
