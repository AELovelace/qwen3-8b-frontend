# rollback\_define\_player

This function defines the object that should be used for players in multiplayer. This is optional, and when used, the system will automatically create instances for players that connect, and destroy instances for players that disconnect.

By default, this creates player instances in the "Instances" layer, which must exist in your game room. If you wish to use another layer, pass its name as the second argument.

For information on creating a game with or without this function, see [Defining A Player Object](../Rollback_System.md#h1). If used, this function must run before the [join](rollback_join_game.md)/[create](rollback_create_game.md) function.

Each instance created with this function gets the [instance variables listed on this page](../Rollback_Variables/Rollback_Variables.md).

 

#### Syntax:

rollback\_define\_player(object, \[layer\_name])

| Argument | Type | Description |
| --- | --- | --- |
| object | [Object Asset](../../../../../The_Asset_Editors/Objects.md) | The object that will be used for creating player instances. |
| layer\_name | [String](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | OPTIONAL The name of the layer where the player instances will be created. "Instances" by default. |

 

#### Returns:

N/A

 

#### Example:

rollback\_define\_player(obj\_player);  

 var \_joined \= rollback\_join\_game();  

  

 if (!\_joined)  

 {  

     rollback\_start\_game(2, false);  

 }
 

The above code defines a player object, and then attempts to join a game. If it was not joined, it starts a new game instead, with a maximum of 2 players and Sync Test disabled.
