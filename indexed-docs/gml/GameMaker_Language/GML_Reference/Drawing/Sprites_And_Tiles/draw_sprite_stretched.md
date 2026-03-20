# draw\_sprite\_stretched

This function simply takes a sprite resource and stretches it over the given width and height so that it occupies that area. As with [draw\_sprite()](draw_sprite.md) you can specify a sprite and a sub\-image for drawing, then the x / y position in the room for the sprite to be drawn at and finally a width and a height (which must be pixel values). The image below shows the result of this function with different sets of arguments:

NOTE When drawing with this function, the sprite [x offset](../../Asset_Management/Sprites/Sprite_Instance_Variables/sprite_xoffset.md) and [y offset](../../Asset_Management/Sprites/Sprite_Instance_Variables/sprite_yoffset.md) (or origins) are ignored and the sprite is drawn with the top\-left corner at the specified x/y position in the room.

 

 

#### Syntax:

draw\_sprite\_stretched(sprite, subimg, x, y, w, h)

| Argument | Type | Description |
| --- | --- | --- |
| sprite |  | The sprite to draw. |
| subimg |  | The subimg (frame) of the sprite to draw (image\_index or \-1 correlate to the current frame of animation in the object). |
| x |  | The x coordinate of where to draw the sprite. |
| y |  | The y coordinate of where to draw the sprite. |
| w |  | The width of the area the stretched sprite will occupy. |
| h |  | The height of the area the stretched sprite will occupy. |

 

#### Returns:

N/A

 

#### Example:

draw\_sprite\_stretched(sprite\_index, image\_index, x, y, sprite\_width, sprite\_height / 2\);

This will draw the instance's assigned sprite and its sub\-image with the left corner at the instance x/y position. Its width is set to the same as the sprite, and the height is the sprite height divided by two.
