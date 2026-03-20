# video\_get\_status

This function returns the status of the currently loaded video. The status can be any one of the following constants:

| [Video Status Constant](video_get_status.md) | |
| --- | --- |
| Constant | Description |
| video\_status\_closed | No video is currently loaded, or the video was closed with [video\_close()](video_close.md) |
| video\_status\_preparing | The video is currently preparing and has not started playing yet |
| video\_status\_playing | The video is currently playing |
| video\_status\_paused | The video is paused (see [video\_pause()](video_pause.md)) |

 

#### Syntax:

video\_get\_status()

 

#### Returns:

[Video Status Constant](video_get_status.md)

 

#### Example:

var \_status \= video\_get\_status();  

  

 if (keyboard\_check\_pressed(vk\_space))  

 {  

     if (\_status \=\= video\_status\_playing)  

     {  

         video\_pause();  

     }  

     else if (status \=\= video\_status\_paused)  

     {  

         video\_resume();  

     }  

 }
 

The above code gets the status of the video and then checks if the player has pressed Space. In that case it pauses the video if it's playing, and resumes it if it's paused.
