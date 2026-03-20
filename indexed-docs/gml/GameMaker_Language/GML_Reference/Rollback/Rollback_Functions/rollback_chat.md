# rollback\_chat

This function is used to send a string message to other players.

You specify a string to send, with a maximum [size](../../Strings/string_byte_length.md) of 128 bytes.

When the second argument is not specified, the message is sent to all players, including the sender.

You can specify a player ID in the second argument which is the player who will receive the message.

### How to Use?

This function is meant to be used "locally", and so would result from [local input](../../Game_Input/Keyboard_Input/Keyboard_Input.md), not [Rollback inputs](rollback_get_input.md).

See the usage example at the bottom. Listen for received messages in the [Rollback Event](../Rollback_Events.md#h1) event. 

 

#### Syntax:

rollback\_chat(message, \[to])

| Argument | Type | Description |
| --- | --- | --- |
| message | [String](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The message to send, as a string. |
| to | [Real](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | OPTIONAL The ID of the player to which the message will be sent. Not specifying this argument, or specifying \-1, sends the message to all players. |

 

#### Returns:

N/A

 

#### Example:

if (keyboard\_check\_pressed(vk\_enter))  

 {  

     rollback\_chat(keyboard\_string);  

     keyboard\_string \= "";  

 }

If the enter key is pressed locally, the [keyboard\_string](../../Game_Input/Keyboard_Input/keyboard_string.md) value is sent to all players. That string is then cleared so a new message can be typed.

This will trigger the [Rollback Event](../Rollback_Events.md#h1) event when the message is received by all clients (including the sender).

Rollback Event

if (rollback\_event\_id \=\= rollback\_chat\_message)  

 {  

     // Get received information  

     var \_message \= rollback\_event\_param.message;  

     var \_from \= rollback\_event\_param.from;  

  

     // Find sender's name  

     var \_name \= rollback\_get\_info(\_from).player\_name;  

  

     // Print to output log  

     show\_debug\_message(\_name \+ " says: " \+ \_message);  

 }
