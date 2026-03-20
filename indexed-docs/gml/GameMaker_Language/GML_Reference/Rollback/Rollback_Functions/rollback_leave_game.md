# rollback\_leave\_game

This function leaves the current multiplayer session, allowing the player to join or create a new game again.

When the host of a room leaves, ownership of that room is transferred to another player, so the game can continue. The game only ends when all the players have left.

### Avoiding Errors

After the player leaves a multiplayer session, GameMaker continues to execute all game code, however it returns to the "pre\-start" state where you cannot create or modify managed instances.

This means you need to manually destroy your player instances on leaving a game, and pause any other game logic using [rollback\_game\_running](../Rollback_Variables/rollback_game_running.md) in a condition, to avoid errors.

See: [State Before Rollback Start](../Rollback_Constraints.md#h1)

### Triggered Event

When a player leaves a game that you are present in, the **Rollback Event** event is triggered. See [Rollback Events](../Rollback_Events.md) for more information.

 

#### Syntax:

rollback\_leave\_game()

 

#### Returns:

N/A

 

#### Example:

if (keyboard\_check\_pressed(vk\_escape))  

 {  

     rollback\_leave\_game();  

 }

The code above makes the player leave the game when the Escape key is pressed.
