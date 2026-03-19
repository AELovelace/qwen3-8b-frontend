# player\_type

This variable tells whether the player instance is a signed\-in GX.games user, or a guest. It can return any one of the following strings:

| String | Description |
| --- | --- |
| "Guest" | The player is not signed into GX.games |
| "User" | The player is signed into GX.games |

Guest users get placeholder [avatars](player_avatar_s.md) and [names](player_.md).

This variable only exists in player instances created by [rollback\_define\_player()](../Rollback_Functions/rollback_define_player.md), and is different for each player.

 

#### Syntax:

player\_type

 

#### Returns:

[String](../../../../../GameMaker_Language/GML_Overview/Data_Types.md)
