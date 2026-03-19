# rollback\_define\_input

This function is used to define custom inputs for all players. It takes a struct which should contain all inputs with their assigned input constants.

To know how to assign custom inputs, see [Custom Controls](../Defining_Inputs.md#h).

If used, this function must run before the [join](rollback_join_game.md)/[create](rollback_create_game.md) function.

 

#### Syntax:

rollback\_define\_input(input\_struct)

| Argument | Type | Description |
| --- | --- | --- |
| input\_struct | [Struct](../../../../../GameMaker_Language/GML_Overview/Structs.md) | A struct containing input names as variables, and their assigned inputs as values. |

 

#### Returns:

N/A

 

#### Example:

rollback\_define\_input({  

     fire: mb\_left,  

     interact: vk\_space,  

     left: \[ord("A"), vk\_left],  

     right: \[ord("D"), vk\_right]  

 });

The code above defines custom inputs for all players. The last two inputs use multiple controls, by listing them in an array.

For an extended example, see [Defining Inputs](../Defining_Inputs.md).
