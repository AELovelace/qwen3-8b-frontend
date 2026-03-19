# rollback\_game\_running

This global variable indicates whether the rollback game is currently running. If this is true, it means the rollback game has started and is currently running. At all other times, it will be false.

 

#### Syntax:

rollback\_game\_running

 

#### Returns:

[Boolean](../../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

if (!rollback\_game\_running) return;  

  

 x \+\= move\_x;  

 y \+\= move\_y;
 

The above code would run in the Step event of a player object. When the rollback game is not running, it would exit the event, so the player can't be controlled until the rollback game has started.
