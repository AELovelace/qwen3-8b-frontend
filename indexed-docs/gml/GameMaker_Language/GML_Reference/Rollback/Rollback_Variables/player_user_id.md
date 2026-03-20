# player\_user\_id

This variable stores the GX.games ID of the current player instance, for use with direct API calls to the [server](rollback_.md).

This variable only exists in player instances created by [rollback\_define\_player()](../Rollback_Functions/rollback_define_player.md), and is different for each player.

[Guest players](player_type.md) will have an empty string assigned to this variable.

 

#### Syntax:

player\_user\_id

 

#### Returns:

[String](../../../../../GameMaker_Language/GML_Overview/Data_Types.md)
