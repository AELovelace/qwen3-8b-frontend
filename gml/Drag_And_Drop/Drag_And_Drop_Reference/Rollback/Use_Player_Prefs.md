# title

This action enables player preferences, and allows you to set the default preferences for all players.

The default preferences can be of any type. If you don't specify default preferences, then all players need to have [preferences set](Set_Player_Prefs.md) before the game can start.

Running this action will disable auto\-start, so you have to [start the game](Start_Game.md) manually. See: [Manual vs. Auto Start](../../../GameMaker_Language/GML_Reference/Rollback/Rollback_System.md#h4)

If used, this action must run before the [join](Join_Game.md)/[create](Create_Game.md) action.

Please read: [Player Preferences](../../../GameMaker_Language/GML_Reference/Rollback/Rollback_Preferences.md)

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Default Prefs | OPTIONAL The default preferences to set for all players. |

#### Example:

This enables player preferences, and sets the default preferences in a struct.
