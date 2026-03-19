# audio\_master\_gain

With this function you can set the absolute value for the global volume of all sounds and music.

It is based on a linear scale from 0 (silent) to any value greater than 0, although normally you'd consider the maximum volume as 1\. Anything over 1 can be used but, depending on the sound used and the platform being compiled to, you may get distortion or clipping when the sound is played back. This function will affect the relative volume of all sounds and music played from within your game.

  This function sets the master gain of the *default* listener. Use [audio\_set\_master\_gain](audio_set_master_gain.md) to set the master gain for a specific listener.

 
 
 

#### Syntax:

audio\_master\_gain(gain)

| Argument | Type | Description |
| --- | --- | --- |
| gain | [Real](../../../GML_Overview/Data_Types.md) | Value for the global volume (0 to 1\) |

 

#### Returns:

N/A

 

#### Example:

if (keyboard\_check(vk\_up))  

 {  

     if vol \< 1 vol \+\= 0\.05;  

     audio\_master\_gain(vol);  

 }  

 if (keyboard\_check(vk\_down))  

 {  

     if vol \> 0 vol \-\= 0\.05;  

     audio\_master\_gain(vol);  

 }

The above code checks for key\-presses of the up and down arrow keys, which then increase or decrease the variable "vol". This variable is then used to set the global gain of all sound and music in the game.
