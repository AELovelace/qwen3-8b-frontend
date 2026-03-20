# rollback\_get\_player\_prefs

This function returns the preferences set for the given player ID.

If a player ID is not specified, the function must be called inside a player instance, in which case the preferences for that player will be returned.

You can also use the instance variable [player\_prefs](../Rollback_Variables/player_prefs.md).

This function returns the last preferences that were synchronised for the given player, so setting the preferences will not immediately update the preferences that this function returns.

Please read: [Player Preferences](../Rollback_Preferences.md)

 

#### Syntax:

rollback\_get\_player\_prefs(\[player\_id])

| Argument | Type | Description |
| --- | --- | --- |
| player\_id | [Real](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | OPTIONAL The ID of the player for which preferences are returned. |

 

#### Returns:

[Any](../../../../../GameMaker_Language/GML_Overview/Data_Types.md#variable)

 

#### Example:

var \_my\_prefs \= rollback\_get\_player\_prefs();  

  

 image\_index \= \_my\_prefs.character;
 

The above code gets the preferences set for the current player, and applies a preference to an instance variable.
