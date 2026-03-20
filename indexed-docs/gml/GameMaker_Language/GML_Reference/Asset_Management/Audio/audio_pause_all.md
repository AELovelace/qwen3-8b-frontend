# audio\_pause\_all

With this function you can pause all sounds that are currently playing.

 

#### Syntax:

audio\_pause\_all()

 

#### Returns:

N/A

 

#### Example:

if (keyboard\_check\_pressed(ord("P")))  

 {  

     global.Pause \= !global.Pause;  

     if (global.Pause)  

     {  

         audio\_pause\_all();  

     }  

     else  

     {  

         audio\_resume\_all();  

     }  

 }

The above code checks for a press of the keyboard key "P" and if it detects one it sets the global variable "Pause" to true or false and then either pauses all sounds or restarts all previously paused sounds.
