# player\_local

When you use [rollback\_define\_player()](../Rollback_Functions/rollback_define_player.md) to define a player object, the system automatically creates an instance of that object for each player. Each instance of that object gets the player\_local variable, which tells whether that player instance is local or not.

If you do not use rollback\_define\_player(), then this variable will not be created for any objects.

You can use this variable for showing which player is local. It's not recommended to use this variable in a way that affects your game logic, which should be the same for local and remote players.

 

#### Syntax:

player\_local

 

#### Returns:

[Boolean](../../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

// Draw event  

 if (player\_local)  

 {  

     draw\_sprite(spr\_arrow, 0, x, y \- 60\);  

 }

The code above runs in the Draw event, and checks if the player instance is local. In that case, it draws an arrow sprite above the instance, telling the player which instance they are controlling.
