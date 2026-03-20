# game\_set\_speed

This function can be used to set the game speed. You can set this in one of two ways \- as either game frames per second (FPS) or as microseconds per game frame (MPF) \- using one of the following two constants:

| Constant | Description |
| --- | --- |
| gamespeed\_fps | Sets the game speed using frames per second. |
| gamespeed\_microseconds | Sets the game speed using microseconds per frame. |

So, for example, a game speed of 30 frames per second would be 33333 microseconds per game frame, which would then be expressed by this function as either:

game\_set\_speed(30, gamespeed\_fps);

or:

game\_set\_speed(33333, gamespeed\_microseconds);

  On Android, if the device's refresh rate cannot be set to the requested game speed, GameMaker will set it to an integer multiple of the requested game speed. If no multiple is available the highest refresh rate available is used and frames are skipped.

  Use [display\_set\_timing\_method](../Cameras_And_Display/display_set_timing_method.md) with tm\_systemtiming if you want to remove a frame rate limit from your game.

 

#### Syntax:

game\_set\_speed(speed, type)

| Argument | Type | Description |
| --- | --- | --- |
| speed | [Real](../../GML_Overview/Data_Types.md) | The new game speed (as either FPS or MPF). |
| type | [Game Speed Constant](game_get_speed.md) | The type of method used to set the game speed (see the constants above). |

 

#### Returns:

N/A

 

#### Example:

if (os\_browser \=\= browser\_not\_a\_browser)  

 {  

     game\_set\_speed(60, gamespeed\_fps);  

 }  

 else  

 {  

     game\_set\_speed(30, gamespeed\_fps);  

 }

The above code checks to see if the game is running in a browser and sets the game speed accordingly as an FPS value.
