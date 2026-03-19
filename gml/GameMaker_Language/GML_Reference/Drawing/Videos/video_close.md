# video\_close

This function closes the video file that is currently loaded. Ensure that this is only called after a [video\_open()](video_open.md) call, otherwise it will not do anything.

 

#### Syntax:

video\_close()

 

#### Returns:

N/A

 

#### Example:

if (keyboard\_check\_pressed(vk\_escape))  

 {  

     video\_close();  

 }

The above code closes the video when the Escape key is pressed.
