# Draw Sprite

This action will draw a sprite somewhere in the room. You specify the sprite, the position (either an absolute position within the room, or a relative position to the instance doing the drawing) and the animation frame of the sprite, if it has multiple frames (note that image frames are numbered from 0 upwards). If you have an animated sprite and you want it to draw the frames as if it was assigned to the object, then use \-1 for the frame index or the built\-in instance variable [image\_index](../../../GameMaker_Language/GML_Reference/Asset_Management/Sprites/Sprite_Instance_Variables/image_index.md), but note that if the instance has no sprite assigned then it will not animate, and if the sprite assigned has a different number of frames to the one being drawn then the sprite will be drawn with extra frames or missed frames.

This action will not draw the sprite transformed, even if you have changed the image blend or scale. For that see the action [Draw Sprite Transformed](Draw_Sprite_Transformed.md).

 
 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Sprite | The sprite to draw |
| x | The x position to draw at |
| y | The y position to draw at |
| Frame Index | The frame index to draw |

 

#### Example:

The above action block code draws a "shadow" sprite at the same relative position as the instance, then draws the instance sprite over the top.
