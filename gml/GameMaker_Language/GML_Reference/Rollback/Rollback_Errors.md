# Rollback Errors

When working with the Rollback system there are certain errors that may occur. These errors are [Runner Errors](../../../Additional_Information/Errors/Runner_Errors.md) and so they are shown while the game is running: 

The following table lists the possible errors that you may get when working with the Rollback system and a description. It also provides a solution for every specific error message.

| Error | Description |
| --- | --- |
| Could not get the layer to create players. You should pass layer name to the rollback\_define\_player function or create Instances layer. | If the player object was defined with [rollback\_define\_player](Rollback_Functions/rollback_define_player.md) function, the rollback system will try to create the player object on the layer, of which the name can optionally be passed as a second parameter (or on the layer with name "Instances" if not defined). If the layer couldn't be found by its name this error is fired. The solution is to either explicitly set the layer name to create the players on or to create a layer with name "Instances" if you don't set the layer name explicitly. |
| Player objects must be managed when running multiplayer games. | If the player object was defined with [rollback\_define\_player](Rollback_Functions/rollback_define_player.md) function and the player object is not flagged as managed this error is fired. The solution is to mark the player object as managed in the [Object Editor](../../../The_Asset_Editors/Objects.md). |
| Failed to get user info for player\_id N. | If the rollback system wasn't able to get information from the server about the player this error is fired. Check the developer console to see if any requests were blocked. |
| Could not call rollback\_chat before fully connected to the game. Try waiting for the rollback\_game\_info event. | The chat function is not available until the player has joined the room. Solution: Disable chat until rollback\_game\_info event received (See [Rollback Events](Rollback_Events.md)). |
| rollback\_use\_manual\_start must be called before rollback\_create\_game and rollback\_join\_game. | These errors are fired if a function call violates internal state machine constraints. The error message suggests a solution. |
| rollback\_use\_player\_prefs must be called before rollback\_create\_game and rollback\_join\_game. |
| rollback\_use\_player\_prefs must be called before rollback\_set\_player\_prefs. |
| rollback\_set\_player\_prefs has to be called before rollback\_start\_game. |
| rollback\_use\_player\_prefs must be called before rollback\_get\_player\_prefs. |
| rollback\_define\_player must be called before rollback\_create\_game and rollback\_join\_game. |
| rollback\_define\_input must be called before rollback\_create\_game and rollback\_join\_game. |
| rollback\_define\_mock\_input must be called before rollback\_create\_game and rollback\_join\_game. |
| Do not read player info before the game has started. Call to rollback\_get\_info(). |
| Do not read player input before the game has started. Call to rollback\_get\_input(). |
| rollback\_define\_input\_frame\_delay must be called before rollback\_create\_game and rollback\_join\_game |
| rollback\_define\_input\_frame\_delay must be called before rollback\_create\_game and rollback\_join\_game. |
| rollback\_set\_player\_prefs failed to set the preferences | The server rejected the player prefs. Usually this happens in the following cases: 1\. One user tries to reset player prefs while the other user already started the game. In this case the game should use the last successfully set user prefs, we guarantee that each player should set some user prefs before the game can be started. 2\. The serialised player prefs size exceeds the max player prefs size (currently 800 bytes). |
| rollback\_create\_game, number of players set to N but must be in the range 1 to 4 | The [rollback\_create\_game](Rollback_Functions/rollback_create_game.md) function was called with a wrong number of players set. The solution is to fix the first parameter of [rollback\_create\_game](Rollback_Functions/rollback_create_game.md) to be in the range from 1 to 4\. |
| rollback\_create\_game failed to set the default player preferences. | See the description for "rollback\_set\_player\_prefs failed to set the preferences" |
| Multiplayer rollback is only supported in the operagx target. | The [rollback\_create\_game](Rollback_Functions/rollback_create_game.md) function is called and the target is not set to OperaGX. Currently multiplayer is supported only on the OperaGX platform. The solution is to set the target to OperaGX. |
| Failed to create a game (unknown session type). | This is an internal error of the rollback system. [Report an issue](https://gamemaker.io/en/contact-us#bug) to the GameMaker team. |
| Could not find player\_id on this instance, you need to pass it in to rollback\_get\_input(). | [rollback\_get\_input](Rollback_Functions/rollback_get_input.md) function may accept player id as a parameter. If no parameters were provided to the function it will take player\_id field of a player object to get inputs. If player\_id parameter is not set this error is fired. If player object was created with [rollback\_define\_player](Rollback_Functions/rollback_define_player.md) it should have player\_id set. Solution: 1\. Explicitly pass player id parameter to the function 2\. Create player with [rollback\_define\_player](Rollback_Functions/rollback_define_player.md). |
| Info player\_id N is out of range. | [rollback\_get\_info](Rollback_Functions/rollback_get_info.md) is called with wrong player\_id (or player object has wrong value in the player\_id field). Solution: Fix player\_id parameter to be in range from 1 to 4\. |
| Couldn't find instance \ of object \ (\) referenced in rollback data. | Internal error of the rollback system.  [Report an issue](https://gamemaker.io/en/contact-us#bug) to the GameMaker team. |
| No idea how to create OBJECT\_KIND\=\. |
| RefID \ has no object (malformed input?). |
| Invalid ReferenceKind \ (malformed input?). |
| Instance mapping is enabled but we tried to deserialise an out of range index. \ is not in \[0, \]. |
| Invalid RValue in deserialisation. |
| Trying to resurrect an instance which has been deleted! |
| Can't serialize RValue with kind\=\ (\). |
| Empty input definition. | [rollback\_define\_input](Rollback_Functions/rollback_define_input.md) was called with an empty input. |
| Input definition contains constant \ twice which is not allowed. | A key code can only be mapped to a single input. Check if any key code is set more than once in the input definition. |
| Input definition with label \ is not a real value or array of reals. | All the values describing input values should have type [Real](../../GML_Overview/Data_Types.md). |
| Empty mock input definition for player\_id N. | See "Empty input definition." |
| Mock definition contains non\-real value. | See "Input definition with label \ is not a real value or array of reals." |
