# video\_set\_volume

This function changes the audio volume of the video that is currently loaded. It takes a value between 0 and 1, where 0 is silent and 1 is the maximum volume.

Ensure that this is only called after a [video\_open()](video_open.md) call but before a [video\_close()](video_close.md) call, otherwise it will not do anything (as there will not be a video loaded).

On some platforms, this function will only work after the video has been loaded completely, so use [Async Callbacks](Videos.md#h) to find out when the video is ready and then change the volume.

 

#### Syntax:

video\_set\_volume(value)

| Argument | Type | Description |
| --- | --- | --- |
| value | [Real](../../../../../GameMaker_Language/GML_Overview/Data_Types.md) | Volume value between 0 and 1 |

 

#### Returns:

N/A

 

#### Example:

my\_video \= video\_open("splash.mp4");  

 video\_set\_volume(0\.5\);

The code above loads splash.mp4 from the Included Files of the game, and changes its volume to 0\.5 (50% of its maximum volume).
