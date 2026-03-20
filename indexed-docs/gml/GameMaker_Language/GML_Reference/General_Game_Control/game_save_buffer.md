# game\_save\_buffer

This is a variant of the [game\_save](game_save.md) function, so please read [its page](game_save.md) first as it contains important information related to its use and to this function's as well.

With this function you can save the current state of the game to a previously created "grow" buffer (see [Buffers](../Buffers/Buffers.md)) which can then be loaded again at any time using the [game\_load\_buffer](game_load_buffer.md) function. This function is designed for use in a single room at a time (i.e.: it's not advised to do a buffer save in one room, then try and load the buffer from another one) and should ideally be used only for checkpoints or level restarts.

  This function is *very* limited and it is designed for the beginner to get a checkpoint system up and running quickly, but more advanced users may prefer to code their own system using the [File](../File_Handling/File_Handling.md) functions, due to the fact that the game will *not* save any of the dynamic resources like data structures, surfaces, added sprites etc.

 

#### Syntax:

game\_save\_buffer(buffer)

| Argument | Type | Description |
| --- | --- | --- |
| buffer | [Buffer](../../../../GameMaker_Language/GML_Reference/Buffers/buffer_create.md) | The buffer to save to. |

 

#### Returns:

N/A

 

#### Example:

if (keyboard\_check\_pressed(ord("S")))   

 {  

     global.Checkpoint \= true;  

     game\_save\_buffer(save\_buff);  

 }

The above code will set a global variable to true and then save the current game state to the buffer stored in the variable "save\_buff" when the key "S" is pressed.
