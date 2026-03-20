# Rollback Preferences

You might want to allow each player to select a character, or customise its properties. Such properties can be set up as "player preferences".

## How To Use Preferences

First, enable preferences by calling [rollback\_use\_player\_prefs()](Rollback_Functions/rollback_use_player_prefs.md) / [Use Player Prefs (Rollback)](../../../Drag_And_Drop/Drag_And_Drop_Reference/Rollback/Use_Player_Prefs.md). With this function you can optionally set the default preferences for all players.

Once you call that function, "auto\-start" is disabled, meaning the game won't start even when all players have joined, and you'll have to start it manually with [rollback\_start\_game()](Rollback_Functions/rollback_start_game.md) / [Start Rollback Game](../../../Drag_And_Drop/Drag_And_Drop_Reference/Rollback/Start_Game.md).

Before the game has started, you can set the preferences for a player by calling [rollback\_set\_player\_prefs()](Rollback_Functions/rollback_set_player_prefs.md) / [Set Player Prefs (Rollback)](../../../Drag_And_Drop/Drag_And_Drop_Reference/Rollback/Set_Player_Prefs.md) on that player's client. These can later be read through [rollback\_get\_player\_prefs()](Rollback_Functions/rollback_get_player_prefs.md) / [Get Player Prefs (Rollback)](../../../Drag_And_Drop/Drag_And_Drop_Reference/Rollback/Get_Player_Prefs.md), or the player\_prefs variable in a player instance.

## Rollback Event

When a player changes its preferences, everyone in the game receives a rollback\_player\_prefs [Rollback Event](Rollback_Events.md#h1). The player must be completely connected for the event to be sent.

If preferences were set before connecting, then on completing the connection, the last preferences set before connecting are sent to all players.

## Start Condition

If you've enabled preferences, and there are no default preferences set, then the game **will not** start unless the preferences for all players have been set.

In such a case, you can either call [rollback\_start\_game()](Rollback_Functions/rollback_start_game.md) repeatedly in an alarm to try starting the game, or call it whenever the rollback\_player\_prefs [Rollback Event](Rollback_Events.md#h1) is received.

## Data Types and Limit

A preference can be of any type, e.g. a number, string, array, etc., but it's recommended to use a [struct](../../GML_Overview/Structs.md), which is the easiest way to store a collection of variables.

The maximum size of a preference payload is 800 bytes, meaning the data you can send as a preference must be 800 bytes or less. If you're sending a struct, you can [convert it to a JSON string](../File_Handling/Encoding_And_Hashing/json_stringify.md) and [get its byte size](../Strings/string_byte_length.md) to get an idea of its size. However, in most cases, structs sent directly (i.e. without being converted into JSON) will have a smaller size than their JSON equivalent, due to the way they are encoded internally.
