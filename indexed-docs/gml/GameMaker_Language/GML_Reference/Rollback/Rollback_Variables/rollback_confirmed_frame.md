# rollback\_confirmed\_frame

This global variable stores the last frame number where inputs for all players were synchronised and confirmed.

You can compare this to [rollback\_current\_frame](rollback_current_frame.md) to check if the current frame has confirmed inputs for all players.

You can also use the function [rollback\_sync\_on\_frame()](../Rollback_Functions/rollback_sync_on_frame.md) to check if the current frame is synchronised.

 

#### Syntax:

rollback\_confirmed\_frame

 

#### Returns:

[Real](../../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

var \_is\_frame\_confirmed \= (rollback\_current\_frame \=\= rollback\_confirmed\_frame);  

  

 if (\_is\_frame\_confirmed)  

 {  

     evaluate\_game\_over();  

 }
 

This code checks if the current frame has confirmed inputs from all players, by checking if the [current frame value](rollback_current_frame.md) is equal to the **confirmed frame value**.

If that is true, it runs a function to check if the game over condition has been satisfied, so it can end the game.

This is done to avoid a prediction\-based state ending the game, and waits for a fully synchronised frame before attempting to check game over conditions.
