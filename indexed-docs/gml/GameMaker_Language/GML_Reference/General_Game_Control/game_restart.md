# game\_restart

This function restarts the game.

Restarting the game is essentially the same as running it for the first time and so the [Game Start Event](../../../The_Asset_Editors/Object_Properties/Other_Events.md) will be triggered *as well as* the [Game End Event](../../../The_Asset_Editors/Object_Properties/Other_Events.md).

All time sources created by [call\_later](../Time_Sources/call_later.md) are destroyed upon restarting the game.

 
It should be noted that certain things will **not** be reset when this function is called:

- [Global Variables](../../GML_Overview/Variables/Global_Variables.md) will not be re\-initialised unless explicitly coded as such \- for example, the built\-in global variable [score](../../GML_Overview/Variables/Builtin_Global_Variables/score.md) will not start at zero after a game restart if it has been modified in the game already.
- The [GPU state](../Drawing/GPU_Control/gpu_get_state.md "gpu_get_state()") will not be changed (so if you have set the draw colour or alpha, for example, it will remain at the changed value).
- The [game speed](game_get_speed.md "game_get_speed()") will remain at whatever you set it in your game code (if you changed it this change will be perpetuated).
- Any asset from the Asset Browser that has been changed at run time within the game \- for example if you change the origin of a sprite asset or shift the position of a path asset \- will *not* be reset.
- Dynamic resources like buffers, surfaces, data structures or imported sprites will also not be cleaned up or removed (although you may lose references to them, so take care when using this function to either use global references for the dynamic resource, or to clean them up before the function is called).
	- This also includes [Flex Panels](../Flex_Panels/Flex_Panels.md) created at runtime, however panels that are part of [UI Layers](../../../The_Asset_Editors/Room_Properties/UI_Layers.md) will be reset

 

#### Syntax:

game\_restart()

 

#### Returns:

N/A

 

#### Example:

if keyboard\_check\_pressed(ord("R"))  

 {  

     game\_restart();  

 }

This code restarts the game when the player presses the "R" key.
