# rollback\_use\_player\_prefs

This function enables player preferences, and allows you to set the default preferences for all players.

The default preferences can be of any type. If you don't specify default preferences, then all players need to have [preferences set](rollback_set_player_prefs.md) before the game can start.

Calling this function will disable auto\-start, so you have to [start the game](rollback_start_game.md) manually. See: [Manual vs. Auto Start](../Rollback_System.md#h4)

If used, this function must run before the [join](rollback_join_game.md)/[create](rollback_create_game.md) function.

Please read: [Player Preferences](../Rollback_Preferences.md)

 

#### Syntax:

rollback\_use\_player\_prefs(\[default])

| Argument | Type | Description |
| --- | --- | --- |
| default | [Any](../../../../../GameMaker_Language/GML_Overview/Data_Types.md#variable) | OPTIONAL The default preferences to set for all players. |

 

#### Returns:

N/A

 

#### Example:

rollback\_use\_player\_prefs({  

     character: 0,  

     color: c\_white  

 });

The above code enables player preferences, and sets the default preferences in a struct.
