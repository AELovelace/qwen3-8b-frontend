# rollback\_join\_game

This function attempts to join a game. You must be on a URL that contains the ID of the virtual room to join.

If a room was joined, it returns true, and if no game was joined, it returns false.

When a new player joins a game that you are already present in, the **Rollback Event** event is triggered. See [Rollback Events](../Rollback_Events.md) for more information.

The dry\_run argument is optional, and when set to true, allows you to run the function without actually joining a game. This is used to check if a game can be joined without actually joining it.

 

#### Syntax:

rollback\_join\_game(\[dry\_run])

| Argument | Type | Description |
| --- | --- | --- |
| dry\_run | [Boolean](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | Disabled by default (false). When enabled (true), the function doesn't join the game, but simply returns true if one can be joined, or false otherwise.   This way you can use this function to only check if the player was invited. |

 

#### Returns:

[Boolean](../../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

rollback\_define\_player(obj\_player);  

 var \_joined \= rollback\_join\_game();  

  

 if (!\_joined)  

 {  

     rollback\_create\_game(2, false);  

 }
 

The above code defines a player object, and then attempts to join a game. If it was not joined, it creates a new game instead, with a maximum of 2 players and Sync Test disabled.

For an extended example, see [Create a Multiplayer Game](../Creating_Multiplayer.md).
