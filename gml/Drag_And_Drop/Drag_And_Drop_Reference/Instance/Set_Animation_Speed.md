# Set Animation Speed

This action block sets the [image\_speed](../../../GameMaker_Language/GML_Reference/Asset_Management/Sprites/Sprite_Instance_Variables/image_speed.md) (animation speed) for the sprite assigned to the instance. You set the ideal frames per second in [The Sprite Editor](../../../The_Asset_Editors/Sprites.md) and then you can use this value to modify it. The default animation speed is set to 1, meaning that the game will try to maintain the number of frames per second that you have defined for the sprite, but you can use values greater than 1 to animate faster (frames may be skipped), or decimal values to animate slower (frames will be shown over various steps) or even negative values to reverse the speed of the animation.

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Speed | The new modifier speed value. |

 

#### Example:

The above action block code sets a new sprite as well as a number of other properties for how that sprite is to be displayed, including setting it to animate at half the defined speed.
