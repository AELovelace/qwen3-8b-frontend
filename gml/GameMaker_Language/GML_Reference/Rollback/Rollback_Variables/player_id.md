# player\_id

When you use [rollback\_define\_player()](../Rollback_Functions/rollback_define_player.md) to define a player object, the system automatically creates an instance of that object for each player. Each instance of that object gets the player\_id variable, which stores the ID of that player.

This ID starts at 0, which initially is the host itself. Any players from 1 and up are "peers" that have joined the game.

If you do not use rollback\_define\_player(), then this variable will not be created for any objects. In that case, player instances and their IDs must be managed manually, as explained in [Defining A Player Object](../Rollback_System.md#h1).

 

#### Syntax:

player\_id

 

#### Returns:

[Real](../../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

// Create event  

 if (player\_id \=\= 0\)  

 {  

     x \= 300;  

 }  

 else if (player\_id \=\= 1\)  

 {  

     x \= 500;  

 }

The code above changes the X position of the player instance based on its ID.

You can also use this ID as an array index, for example, to store scores for all players:

// Step event  

 var \_coin \= instance\_place(x, y, obj\_coin);  

 if (\_coin !\= noone)  

 {  

     obj\_game.scores\[player\_id]\+\+;  

     instance\_destroy(\_coin);  

 }  

  

 // Draw event  

 var \_my\_score \= obj\_game.scores\[player\_id];  

 draw\_text(x, y, \_my\_score);
 

The Step event code above increases the score of the player in an array in obj\_game when it collides with a coin. That coin instance is then destroyed.

The Draw event code above retrieves the player's score from the same array, and draws its value.
