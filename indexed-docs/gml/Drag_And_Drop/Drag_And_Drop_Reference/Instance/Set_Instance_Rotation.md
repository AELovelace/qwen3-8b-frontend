# Set Instance Rotation

This action block sets the [image\_angle](../../../GameMaker_Language/GML_Reference/Asset_Management/Sprites/Sprite_Instance_Variables/image_angle.md) (rotation) of the instance. The angle is measured in degrees, with the right being 0°, up being 90°, left being 180° and down being 270°. Set this variable to 0 to reset the instance, meaning that it will draw any sprite assigned to as it was defined in [The Sprite Editor](../../../The_Asset_Editors/Sprites.md).

  For changes in this action to be visible, the instance should have either *no* draw event (and so GameMaker will default draw the sprite) or be drawn using [Draw Self](../Drawing/Draw_Self.md) action.

 

#### Action Syntax:

#### Arguments:

 

| Argument | Description |
| --- | --- |
| Angle | The new angle to use (from 0 to 360\). |

 

#### Example:

The above action block code sets a new sprite as well as a number of other properties for how that sprite is to be displayed, including rotating it 180°.
