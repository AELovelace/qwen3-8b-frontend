# title

This function is used to pause a GXC recording that was previously started with [gxc\_start\_movie\_recording()](gxc_start_movie_recording.md).

 

#### Syntax:

gxc\_pause\_movie\_recording();

 

#### Returns:

N/A

 

#### Example:

if (keyboard\_check\_pressed(vk\_escape))  

 {  

 gxc\_pause\_movie\_recording();  

 }

This will pause the GXC movie recording if the escape key is pressed.
