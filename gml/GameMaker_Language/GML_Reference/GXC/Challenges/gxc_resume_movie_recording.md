# title

This function is used to resume a GXC recording that was previously paused with [gxc\_pause\_movie\_recording()](gxc_pause_movie_recording.md).

 

#### Syntax:

gxc\_resume\_movie\_recording();

 

#### Returns:

N/A

 

#### Example:

if (keyboard\_check\_pressed(vk\_enter))  

 {  

 gxc\_resume\_movie\_recording();  

 }

This will resume the currently paused GXC movie recording if the enter key is pressed.
