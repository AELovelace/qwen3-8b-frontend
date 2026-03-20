# Rollback Events

There are two Rollback\-related events you can find in the "Other" category:

## Rollback Start

This event is triggered when all the players are connected and the multiplayer game has started. It's also triggered when the room is later changed.

Within this event, you get a struct called rollback\_event\_param which contains all relevant values for the event:

| Struct Member | Description |
| --- | --- |
| num\_players | The total number of players in the game |
| player\_id | The ID of your local player (starting at 0, which initially is the host itself) |
| first\_start | This is true if the multiplayer game just started, or false if only the room was changed |
| late\_join | This is true if the player is a late joining player, or false if not |

You should only use this event in your game manager object rather than a player object, as rollback\_event\_param.player\_id will always be the ID of your main local player and NOT the ID of the player instance that the event may trigger in.

For example, if you are player 0, and you catch the **Rollback Start** event in the instance of player 1, the player\_id variable will still be 0 as it indicates the ID of the local player only.

## Rollback Event

The **Rollback Event** event is triggered at various points throughout the game, containing a rollback\_event\_id variable. This variable indicates what type of event has been triggered.

A struct called rollback\_event\_param is provided which contains all relevant values for the event.

Any one of the following constants may be stored in rollback\_event\_id:

| rollback\_event\_id | Description |
| --- | --- |
| In\-Game | |
| rollback\_chat\_message | Triggered when a message from [rollback\_chat()](Rollback_Functions/rollback_chat.md) / [Send Message (Rollback)](../../../Drag_And_Drop/Drag_And_Drop_Reference/Rollback/Send_Message.md) is received. During this event, rollback\_event\_param will contain the following variables:  message: The message string received from: The ID of the player that sent the message to: The ID of the player that the message was sent to; will be \-1 if the message was sent to everyone |
| rollback\_player\_prefs | Triggered when a player sets its [preferences](Rollback_Preferences.md). During this event, rollback\_event\_param will contain the following variables:  player\_id: The ID of the player that set its preferences preferences: The preferences set for that player |
| Game | |
| rollback\_game\_interrupted | Triggered when the game is interrupted because of a player with an unstable connection. During this event, rollback\_event\_param will contain the following variables:  player\_id: ID of the player with connection issues timeout: How much time is remaining for that player to time out and disconnect (in milliseconds). After this amount of time, the player will be kicked and the game will resume with the remaining players. |
| rollback\_game\_resumed | Triggered when the game resumes after an interruption (as described above). The ID of the player that reconnected is stored in rollback\_event\_param.player\_id. |
| rollback\_game\_full | Triggered when the game/room you are connecting to is already full. |
| rollback\_game\_info | Triggered when information about a room is received, but before it is fully joined.  During this event, rollback\_event\_param will contain the following variables:  num\_players: The total number of players in the game player\_id: The ID of the local player (starting at 0\) |
| Connection | |
| rollback\_end\_game | Triggered when the server wants clients to stop the game. Usually this event means that clients are in an inconsistent state. The multiplayer session is closed automatically before the event is fired. |
| rollback\_connect\_info | Triggered when a room has been created and is ready to be shared with other players. The shareable URL is stored in rollback\_event\_param.share\_url.   You can copy this URL automatically when it becomes available by calling [clipboard\_set\_text()](../Strings/clipboard_set_text.md). |
| rollback\_connect\_error | Triggered when there is a connection error. The rollback\_event\_param [struct](../../GML_Overview/Structs.md) will contain the following variables:  status The HTTP status code of the response error A string describing the error |
| rollback\_connection\_rejected | Triggered when a connection attempt is rejected. The error can be caused by an invalid token, mismatch in client versions, or mismatch in protocol versions. The multiplayer session is closed automatically before the event is fired. |
| rollback\_protocol\_rejected | Triggered when a connection attempt is rejected. This means the client is using an obsolete version of the protocol. Before this event is fired, GameMaker will show an error message in\-game (even if [events are disabled](Rollback_Functions/rollback_display_events.md)). The multiplayer session is closed automatically before the event is fired. |
| rollback\_high\_latency | Triggered when your latency to the server is too high. The multiplayer session is closed automatically before the event is fired. |
| Peers | |
| rollback\_connected\_to\_peer | Triggered when a new player has connected. The ID of the connected player is stored in rollback\_event\_param.player\_id. |
| rollback\_synchronizing\_with\_peer | Triggered while the game is synchronising with a new player. During this event, rollback\_event\_param will contain the following variables:  player\_id: ID of the player that you're synchronizing with count: How many synchronisation steps have been completed total: How many total synchronisation steps need to be completed |
| rollback\_synchronized\_with\_peer | Triggered when synchronisation with a player is complete. The ID of the synchronised player is stored in rollback\_event\_param.player\_id. |
| rollback\_disconnected\_from\_peer | Triggered when a player disconnects. The ID of the disconnected player is stored in rollback\_event\_param.player\_id. |
