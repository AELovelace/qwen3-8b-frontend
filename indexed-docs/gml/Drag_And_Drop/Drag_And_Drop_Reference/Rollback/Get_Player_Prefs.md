# title

This action gets the preferences set for the given player ID, and applies them to the "Target" variable.

If a player ID is not specified, the action must be called inside a player instance, in which case the preferences for that player will be returned.

You can also use the instance variable [player\_prefs](../../../GameMaker_Language/GML_Reference/Rollback/Rollback_Variables/player_prefs.md).

This action returns the last preferences that were synchronised for the given player, so setting the preferences will not immediately update the preferences that this function returns.

Please read: [Player Preferences](../../../GameMaker_Language/GML_Reference/Rollback/Rollback_Preferences.md)

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Player ID | OPTIONAL The ID of the player for which preferences are returned. |
| Target | The variable where the player's preferences will be stored |

#### Example:

This gets the preferences set for the current player, and applies a preference to the instance's colour.
