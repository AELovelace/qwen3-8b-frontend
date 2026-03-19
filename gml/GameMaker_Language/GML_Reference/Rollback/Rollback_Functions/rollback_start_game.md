# rollback\_start\_game

This function forces the current multiplayer game to start, before all players have joined. You must first create a multiplayer game using [rollback\_create\_game()](rollback_create_game.md).

The system normally waits for all players to join before automatically starting the game. This function can be used to start the game early, before all players have joined.

You can call [rollback\_use\_manual\_start()](rollback_use_manual_start.md) to make Rollback wait for this function even after all players have joined.

Calling this function will trigger the [Rollback Start](../Rollback_Events.md#h) event.

 

#### Syntax:

rollback\_start\_game()

 

#### Returns:

N/A

 

#### Example:

// Step event  

 if (!rollback\_game\_running \&\& keyboard\_check\_pressed(vk\_enter))  

 {  

     rollback\_start\_game();  

 }

If the Rollback game is not running, and Enter is pressed, this will start the game.

This allows the player to start the game manually before all players join.
