# draw\_sprite\_part

This function draws part of the given sprite at a given position within the room.

As with [draw\_sprite](draw_sprite.md) you specify a sprite and a sub\-image for drawing, then you give the *relative coordinates* of the *part* of the sprite that you want to draw. The left and top position of the sprite part are specified relative to the sprite's top\-left corner (the sprite's [x offset](../../Asset_Management/Sprites/Sprite_Instance_Variables/sprite_xoffset.md) and [y offset](../../Asset_Management/Sprites/Sprite_Instance_Variables/sprite_yoffset.md) are ignored), with a left position of 0 and a top position of 0 referring to the top\-left corner of the sprite. The width and height determine the area to draw. The function then draws the sprite part with its top\-left corner at the specified (x, y) position in the room.

The image below shows an example of how this works:

 
### Usage Notes

- You should note that if the texture page permits automatic cropping then this function may not work as expected, since the extra "empty" space around the sprite will have been removed for creating the texture page. To resolve this issue, you will need to set the texture page settings (in the [Texture Group Editor](../../../../Settings/Texture_Groups.md)) to disable the option **Automatic Crop**.
- This function is only useful for **bitmap** sprites and will not work with vector or JSON (Spine) sprites.

 

#### Syntax:

draw\_sprite\_part(sprite, subimg, left, top, width, height, x, y)

| Argument | Type | Description |
| --- | --- | --- |
| sprite | [Sprite Asset](../../../../The_Asset_Editors/Sprites.md) | The sprite to draw. |
| subimg | [Real](../../../GML_Overview/Data_Types.md) | The sub\-image (frame) of the sprite to draw ([image\_index](../../Asset_Management/Sprites/Sprite_Instance_Variables/image_index.md) or \-1 correlate to the current frame of animation in the instance). |
| left | [Real](../../../GML_Overview/Data_Types.md) | The x position on the sprite of the top\-left corner of the area to draw. |
| top | [Real](../../../GML_Overview/Data_Types.md) | The y position on the sprite of the top\-left corner of the area to draw. |
| width | [Real](../../../GML_Overview/Data_Types.md) | The width of the area to draw. |
| height | [Real](../../../GML_Overview/Data_Types.md) | The height of the area to draw. |
| x | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate of where to draw the sprite part. |
| y | [Real](../../../GML_Overview/Data_Types.md) | The y coordinate of where to draw the sprite part. |

 

#### Returns:

N/A

 

#### Example:

draw\_sprite\_part(sprite\_index, image\_index, 4, 0, sprite\_width\-16, sprite\_height\-16, x, y);

This will draw the current instance's assigned sprite ([sprite\_index](../../Asset_Management/Sprites/Sprite_Instance_Variables/sprite_index.md)) at its current frame of animation ([image\_index](../../Asset_Management/Sprites/Sprite_Instance_Variables/image_index.md)), however it will shave a 4px margin off the width on both sides, and an 8 pixel margin off the height from the bottom of the original 24x24 pixel sprite.
