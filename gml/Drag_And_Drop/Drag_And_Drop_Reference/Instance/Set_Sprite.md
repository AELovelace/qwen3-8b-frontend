# Set Sprite

This action block sets the [sprite\_index](../../../GameMaker_Language/GML_Reference/Asset_Management/Sprites/Sprite_Instance_Variables/sprite_index.md) of the instance to another sprite from [The Asset Browser](../../../Introduction/The_Asset_Browser.md). You select the sprite to change to, and then give the image (animation frame) to show. Note that if you don't want the sprite to animate after setting the frame, you'll need to use the [Set Animation Speed](Set_Animation_Speed.md) action and set it to 0, or if you want the sprite to continue animating then set the value to use the [image\_index](../../../GameMaker_Language/GML_Reference/Asset_Management/Sprites/Sprite_Instance_Variables/image_index.md) built\-in variable instead.

Changing the sprite will also change the collision mask of the instance, unless you have also specified a separate [mask\_index](../../../GameMaker_Language/GML_Reference/Asset_Management/Sprites/Sprite_Instance_Variables/mask_index.md) in [The Object Editor](../../../The_Asset_Editors/Objects.md).

  For changes in this action to be visible, the instance should have either *no* Draw event (and so GameMaker will default draw the sprite) or be drawn using [Draw Self](../Drawing/Draw_Self.md) action.

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Sprite | The new sprite to use (\-1 if you want to remove the sprite). |
| Frame | The animation frame to show initially (if no extra frames are used, then use 0\). |

 

#### Example:

The above action block code sets a new sprite as well as a number of other properties for how that sprite is to be displayed.
