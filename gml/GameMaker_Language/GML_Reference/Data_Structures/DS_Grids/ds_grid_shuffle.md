# ds\_grid\_shuffle

This function can be used to randomise the positions of all values in all cells within a grid.

**NOTE** This function will shuffle the grid cells to the same positions every time the game is run afresh due to the fact that GameMaker generates the same initial random seed every time to make debugging code a far easier task. To avoid this behaviour use [randomise()](../../Maths_And_Numbers/Number_Functions/randomise.md) at the start of your game. This is only true when testing and debugging the game, as the final executable package will not show this behaviour and will be random every play.

 

#### Syntax:

ds\_grid\_shuffle(index)

| Argument | Type | Description |
| --- | --- | --- |
| index | [DS Grid](ds_grid_create.md) | The handle of the grid to shuffle. |

 

#### Returns:

N/A

 

#### Example:

ds\_grid\_shuffle(grid)

This would take all the values in the DS grid indexed in the variable "grid" and shuffle them around to get a different order.
