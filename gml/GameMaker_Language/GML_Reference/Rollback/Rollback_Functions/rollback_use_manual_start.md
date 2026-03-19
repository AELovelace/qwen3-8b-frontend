# rollback\_use\_manual\_start

By default, a multiplayer game automatically starts when all players have joined.

Calling this function disables that auto\-start behaviour, so the game waits for you to [start it manually](rollback_start_game.md).

If used, this function must run before the [join](rollback_join_game.md)/[create](rollback_create_game.md) function.

 

#### Syntax:

rollback\_use\_manual\_start()

 

#### Returns:

N/A

 

#### Example:

rollback\_use\_manual\_start();  

  

 if (!rollback\_join\_game())  

 {  

     rollback\_create\_game(2\);  

 }
 

The above code enables manual start, and then joins or creates a new multiplayer game.
