# rollback\_get\_input

This function returns a struct containing the input values for a player. It takes an optional argument specifying the ID of the player for which inputs will be returned.

When used in a player instance that was created by [rollback\_define\_player()](rollback_define_input.md), you do not need to specify a player ID, so you can call this function without any arguments.

When used in any other instances, or player instances that were created manually, you must specify a player ID.

For information on what inputs are returned and how they can be changed, see [Defining Inputs](../Defining_Inputs.md).

 

#### Syntax:

rollback\_get\_input(player\_id)

| Argument | Type | Description |
| --- | --- | --- |
| player\_id | [Real](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | OPTIONAL The ID of the player for which inputs will be returned. |

 

#### Returns:

[Struct](../../../../../GameMaker_Language/GML_Overview/Structs.md)

 

#### Example:

var \_input \= rollback\_get\_input();  

  

 if (\_input.left) x \-\= 2;  

 if (\_input.right) x \+\= 2;  

 if (\_input.up) y \-\= 2;  

 if (\_input.down) y \+\= 2;
 

The code above gets the input struct in a player instance that was automatically created by the Rollback system. Based on the returned values, it moves the instance by 2 pixels in each direction.

For an extended example, see [Creating a Multiplayer Game](../Creating_Multiplayer.md).
