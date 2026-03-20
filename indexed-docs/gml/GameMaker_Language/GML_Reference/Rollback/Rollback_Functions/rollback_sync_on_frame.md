# rollback\_sync\_on\_frame

This function checks if all players are synchronised on the current frame, meaning their states are not based on predictions but on the actual data received from them. In such a case, it returns true.

If players are not synchronised on the current frame, it returns false, and attempts to synchronise all players.

Attempting to synchronise players with this function may cause a freeze. You must ensure that this function is not continuously called in a Step event.

Instead, use it as a toggle. See the example at the bottom of the page.

The variable [rollback\_confirmed\_frame](../Rollback_Variables/rollback_confirmed_frame.md) is updated automatically when all players are synchronised.

 

#### Syntax:

rollback\_sync\_on\_frame()

 

#### Returns:

[Boolean](../../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

if (obj\_game.winning\_player \=\= \-1 \&\& points \>\= obj\_game.points\_required\_for\_win)  

 {  

     if (rollback\_sync\_on\_frame())  

     {  

         obj\_game.winning\_player \= player\_id;  

     }  

 }

This code runs in a player object's Step event.

It checks if there is no winning player, and if the current player has the points required for winning.

If both are true, it means the player should win. However, before doing that, it checks if all players are synchronised, to ensure that the state is correct.

If all players are synchronised, it sets the winning\_player variable. This results in the first condition becoming false, ensuring that rollback\_sync\_on\_frame() is not called again.

This means the function is used as a toggle, instead of running continuously every frame.
