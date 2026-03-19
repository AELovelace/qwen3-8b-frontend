# title

This action is used to send a string message to other players.

You specify a string to send, with a maximum [size](../../../GameMaker_Language/GML_Reference/Strings/string_byte_length.md) of 128 bytes.

When the second argument is not specified, the message is sent to all players, including the sender.

You can specify a player ID in the second argument which is the player who will receive the message.

### How to Use?

This action is meant to be used "locally", and so would result from [local input](../Mouse_And_Keyboard/Mouse_And_Keyboard_Actions.md), not [Rollback inputs](Get_Input.md).

See the usage example at the bottom. Listen for received messages in the [Rollback Event](../../../GameMaker_Language/GML_Reference/Rollback/Rollback_Events.md#h1) event. 

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Message | The message to send, as a string. |
| To | OPTIONAL The ID of the player to which the message will be sent. Not specifying this argument, or specifying \-1, sends the message to all players. |

 

#### Example:

If the enter key is pressed locally, the [keyboard\_string](../../../GameMaker_Language/GML_Reference/Game_Input/Keyboard_Input/keyboard_string.md) value is sent to all players. That string is then cleared so a new message can be typed.

This will trigger the [Rollback Event](../../../GameMaker_Language/GML_Reference/Rollback/Rollback_Events.md#h1) event when the message is received by all clients (including the sender).

Example of a Rollback Event to print a received message to the Output Log
