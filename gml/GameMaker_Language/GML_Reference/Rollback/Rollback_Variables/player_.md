# title

This variable stores the name of the current player instance.

This variable only exists in player instances created by [rollback\_define\_player()](../Rollback_Functions/rollback_define_player.md), and is different for each player.

[Guest players](player_type.md) will return a placeholder name.

 

#### Syntax:

player\_name;

 

#### Returns:

[String](../../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

// Draw event  

 draw\_set\_halign(fa\_center);  

 draw\_set\_valign(fa\_middle);  

  

 draw\_text(x, y \- 100, player\_name);  

  

 draw\_set\_valign(fa\_left);  

 draw\_set\_valign(fa\_top);
 

This draws the name of the player 100px above its instance, with a center\-middle alignment.
