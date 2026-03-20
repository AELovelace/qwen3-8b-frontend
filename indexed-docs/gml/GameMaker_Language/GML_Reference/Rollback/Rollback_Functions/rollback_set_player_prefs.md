# rollback\_set\_player\_prefs

After [enabling preferences](rollback_set_player_prefs.md), this function is used to set the preferences for the local player. This means the function must rely on [local input](../../Game_Input/Keyboard_Input/Keyboard_Input.md) and not [Rollback input](rollback_get_input.md).

The preferences can be of any type. If default preferences are set, ensure you use the same data type and structure.

When any player sets its preferences, everyone in the game receives a [Rollback Event](../Rollback_Events.md#h1).

If used, this function must run before the game [starts](rollback_start_game.md).

Please read: [Player Preferences](../Rollback_Preferences.md)

 

#### Syntax:

rollback\_set\_player\_prefs(preferences)

| Argument | Type | Description |
| --- | --- | --- |
| preferences | [Any](../../../../../GameMaker_Language/GML_Overview/Data_Types.md#variable) | The preferences to set for the local player. |

 

#### Returns:

N/A

 

#### Example:

rollback\_set\_player\_prefs({  

     character: obj\_customizer.character\_selected,  

     color: obj\_customizer.color\_selected  

 });

The above code sets the preferences for the player, reading values from a "customizer" object, which would be unmanaged (local).
