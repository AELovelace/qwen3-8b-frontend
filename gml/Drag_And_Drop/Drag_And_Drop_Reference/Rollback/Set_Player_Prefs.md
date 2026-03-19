# title

After [enabling preferences](Use_Player_Prefs.md), this action is used to set the preferences for the local player. This means the function must rely on [local input](../Mouse_And_Keyboard/Mouse_And_Keyboard_Actions.md) and not [Rollback input](Get_Input.md).

The preferences can be of any type. If default preferences are set, ensure you use the same data type and structure.

When any player sets its preferences, everyone in the game receives a [Rollback Event](../../../GameMaker_Language/GML_Reference/Rollback/Rollback_Events.md#h1).

If used, this function must run before the game [starts](Start_Game.md).

Please read: [Player Preferences](../../../GameMaker_Language/GML_Reference/Rollback/Rollback_Preferences.md)

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Prefs | The preferences to set for the local player. |

#### Example:

This sets the preferences for the player, reading values from a "customiser" object, which would be unmanaged (local).
