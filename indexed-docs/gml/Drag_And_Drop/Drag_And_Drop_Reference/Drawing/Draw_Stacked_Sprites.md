# Draw Stacked Sprites

This action will draw a sprite a given number of times one after another at a given position within the room. You give the sprite to draw and the stack order, which can be either **Horizontal** (horizontally, left to right), or **Vertical** (vertically, top to bottom), as well as the number of sprites to draw and the position. The position can be an absolute position within the room, or one relative to the position of the instance doing the drawing, and the spacing between images will be based on the width or height of the sprite. Note that this simply draws a static image \- the initial single image (frame 0\) of the given sprite \- and any further frames will be ignored, as will any transforms that have been added through changing the [instance variables](../Instance/Set_Instance_Variable.md) (like [image\_xscale](../../../GameMaker_Language/GML_Reference/Asset_Management/Sprites/Sprite_Instance_Variables/image_xscale.md) or [image\_blend](../../../GameMaker_Language/GML_Reference/Asset_Management/Sprites/Sprite_Instance_Variables/image_blend.md)).

 
 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Sprite | The sprite to draw |
| Stack Order | The order to draw in (either Horizontal or Vertical) |
| Number | The number of sprites to draw |
| x | The x position to draw at |
| y | The y position to draw at |

 

#### Example:

The above action block code gets the number of instances of the object obj\_Player and then uses this to draw a number of marker sprites to the screen.
