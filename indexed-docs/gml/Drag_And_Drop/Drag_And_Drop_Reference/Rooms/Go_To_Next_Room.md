# title

This action will make your game go to the next room as listed in the [Room Manager](../../../Settings/The_Room_Manager.md) at the time the game was compiled. If this room does not exist, an error will be thrown and the game will be forced
 to close. Note that the room will not change until the end of the event or script where the action was called, so any code after this action will still run.

 

#### Action Syntax:

#### Example:

The above action block code checks for a collision with another object and if one is detected
 a variable in the instance is checked and the game will either go to the next room or the previous room as listed in the Room Manager order.
