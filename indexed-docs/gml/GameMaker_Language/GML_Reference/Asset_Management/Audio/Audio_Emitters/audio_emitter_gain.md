# audio\_emitter\_gain

This function sets the maximum gain (volume) for the emitter. You can fade it over a certain period of time by passing the time argument.

The perceived volume for a sound can change depending on the [fall\-off value](audio_emitter_falloff.md) and the position it has relative to the *listener*, but by setting the gain with this function, the full volume will never exceed the specified gain value. The image below illustrates how gain affects the volume of the emitter when fall\-off is greater than 0:

This function will change the volume of the sound while it is being played as well all subsequent sounds played through the given emitter. Note that on some platforms you can have a gain of greater than 1, although a value of 1 is considered "full volume" and anything greater may introduce audio clipping or distortion.

  The final volume will also be influenced by the global audio gain that has been set by the function [audio\_master\_gain](../audio_master_gain.md).

 
 

#### Syntax:

audio\_emitter\_gain(emitter, gain, \[time])

| Argument | Type | Description |
| --- | --- | --- |
| emitter | [Audio Emitter ID](audio_emitter_create.md) | The index of the emitter to change. |
| gain | [Real](../../../../GML_Overview/Data_Types.md) | The maximum gain (default 1\). |
| time | [Real](../../../../GML_Overview/Data_Types.md) | The length of the change in gain in milliseconds. Defaults to 0 (instantaneous change) if not passed. |

 

#### Returns:

N/A

 

#### Example:

if (up)  

 {  

     gain \+\= 0\.05;  

     if (gain \>\= 1\) up \= false;  

 }  

 else  

 {  

     gain \-\= 0\.05;  

     if (gain \<\= 0\) up \= true;  

 }  

  

 audio\_emitter\_gain(s\_emit, gain);
 

The above code sets the variable gain to different values and then uses that same variable to set the gain of the emitter indexed in the variable s\_emit.
