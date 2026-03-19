# rollback\_get\_info

This function returns a struct containing information about a player. This should only be used when managing player instances manually. If you're using [rollback\_define\_player()](rollback_define_player.md), then each player instance will automatically receive this information as [variables](../Rollback_Variables/Rollback_Variables.md).

The function takes the ID of the player as an argument, and returns a struct with the following variables:

| Variable | Type | Description |
| --- | --- | --- |
| player\_avatar\_url | [String](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | URL pointing to the player's avatar image |
| player\_avatar\_sprite | [Sprite Asset](../../../../../The_Asset_Editors/Sprites.md) | Sprite containing the player's avatar |
| player\_name | [String](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The name of the player |
| player\_type | [String](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | Tells whether the player is signed\-into GX.games or not   Will be "Guest" for guest users, and "User" for signed\-in users |
| player\_user\_id | [String](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The ID of the player on GX.games |
| player\_prefs | [Any](../../../../../GameMaker_Language/GML_Overview/Data_Types.md#variable) | The [preferences](rollback_set_player_prefs.md) set for the player |

 

 

#### Syntax:

rollback\_get\_info(player\_id)

| Argument | Type | Description |
| --- | --- | --- |
| player\_id | [Real](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The ID of the player for which information will be returned. |

 

#### Returns:

[Struct](../../../../../GameMaker_Language/GML_Overview/Structs.md)
