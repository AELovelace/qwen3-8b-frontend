# rollback\_define\_input\_frame\_delay

This function defines the fixed frame delay for local player inputs.

By default, your game will use an adaptive input delay, which is based on the latency between players. This will work for almost every game out there, however, some specific types of games (e.g. fighting games) may prefer to use a fixed input delay, instead of an adaptive delay that may change at any time.

It's not recommended to change this unless you know exactly what you're doing. You can call this function at any time before and during a multiplayer game.

The delay value specified must be in number of frames. If you specify \-1, the game will revert to using an adaptive delay. The maximum delay you can set is **10 frames**.

 

#### Syntax:

rollback\_define\_input\_frame\_delay(frames)

| Argument | Type | Description |
| --- | --- | --- |
| frames | [Real](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The number of frames to set as the fixed input delay, or \-1 to reset it to default. |

 

#### Returns:

N/A

 

#### Example:

// 'Options' script  

 global.frame\_delay \= 5;  

  

 // obj\_game: Create event  

 rollback\_define\_input\_frame\_delay(global.frame\_delay);  

 var \_joined \= rollback\_join\_game();  

  

 if (!\_joined)  

 {  

     rollback\_start\_game(2, false);  

 }
 

You can define your frame delay value as a global variable, and use that when calling rollback\_define\_input\_frame\_delay() before a rollback game is started.
