# video\_is\_looping

This function returns whether the currently loaded video is set to loop (true) or not (false). You can set a video to loop by calling [video\_enable\_loop()](video_enable_loop.md).

 

#### Syntax:

video\_is\_looping()

 

#### Returns:

[Boolean](../../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

if (video\_is\_looping()) {  

     obj\_player.control\_enabled \= false;  

 }

The above code checks if the currently loaded video is looping, and in that case, disables the player's controls, by setting a custom instance variable to false.
