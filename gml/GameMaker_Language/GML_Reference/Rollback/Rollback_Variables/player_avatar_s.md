# title

This variable stores the sprite of the current player instance.

This variable only exists in player instances created by [rollback\_define\_player()](../Rollback_Functions/rollback_define_player.md), and is different for each player.

[Guest players](player_type.md) will display a placeholder sprite.

 

#### Syntax:

player\_avatar\_sprite;

 

#### Returns:

[Sprite Asset](../../../../../The_Asset_Editors/Sprites.md)

 

#### Example:

// Draw event  

 draw\_sprite\_stretched(player\_avatar\_sprite, 0, x, y \- 256, 64, 64\);

This displays the avatar of the player instance running the code, in a 64x64 area, 256px above the instance.
