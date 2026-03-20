# rollback\_define\_mock\_input

This function can be used during [Sync Test](../Rollback_System.md#h) to assign temporary "mock" input to the specified player. This overrides the [controls defined](rollback_define_input.md) for the player and any [random input](rollback_use_random_input.md) from Sync Test.

For information on its use, see [Mock Input](../Defining_Inputs.md#h1).

 

#### Syntax:

rollback\_define\_mock\_input(player\_id, input\_struct)

| Argument | Type | Description |
| --- | --- | --- |
| player\_id | [Real](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The ID of the player to assign mock input to. |
| input\_struct | [Struct](../../../../../GameMaker_Language/GML_Overview/Structs.md) | A struct containing input names as variables, and their assigned inputs as values. |

 

#### Returns:

N/A

 

#### Example:

rollback\_define\_input({  

     fire: mb\_left,  

     interact: vk\_space,  

     left: ord("A"),  

     right: ord("D")  

 });  

  

 rollback\_define\_mock\_input(1, {  

     fire: vk\_control,  

     interact: vk\_shift,  

     left: ord("J"),  

     right: ord("L")  

 });
 

The code above first defines the inputs for players. It then defines mock input for player 1, keeping the same input names but assigning different inputs. This way two people could play the game locally using the keyboard.
