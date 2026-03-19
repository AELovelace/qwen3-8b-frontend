# audio\_emitter\_pitch

This function changes the pitch of the given emitter, affecting the pitch of all sounds played on this emitter.

The emitter pitch is a *pitch multiplier*, in that the input value multiplies the current pitch by that amount, so the default value of 1 is no pitch change, while a value of less than 1 will lower the pitch and greater than 1 will raise the pitch. It is best to use small increments for this function as any value under 0 or over 5 may not be audible anyway.

Sounds already playing on the audio emitter do not have to be restarted in order for the change in pitch to be audible. The change in pitch is **applied immediately**.

 
#### Syntax:

audio\_emitter\_pitch(emitter, pitch)

| Argument | Type | Description |
| --- | --- | --- |
| emitter | [Audio Emitter ID](audio_emitter_create.md) | The index of the emitter to change. |
| pitch | [Real](../../../../GML_Overview/Data_Types.md) |  |

 

#### Returns:

N/A

 

#### Example:

switch (gear)  

 {  

     case 1: audio\_emitter\_pitch(s\_emit, 0\.8\); break;  

     case 2: audio\_emitter\_pitch(s\_emit, 0\.9\); break;  

     case 3: audio\_emitter\_pitch(s\_emit, 0\.95\); break;  

     case 4: audio\_emitter\_pitch(s\_emit, 1\); break;  

     case 5: audio\_emitter\_pitch(s\_emit, 1\.2\); break;  

 }

The above code will change the pitch of the audio played from the emitter indexed in the variable "s\_emit" based on the value of the variable "gear".
