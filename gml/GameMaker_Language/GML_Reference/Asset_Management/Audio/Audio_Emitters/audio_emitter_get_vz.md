# audio\_emitter\_get\_vz

This function returns the current velocity along the z axis for the given audio emitter.

 

#### Syntax:

audio\_emitter\_get\_vz(emitter)

| Argument | Type | Description |
| --- | --- | --- |
| emitter | Audio Emitter ID | The index of the emitter to use. |

 

#### Returns:

Real

 

#### Example:

if (audio\_emitter\_get\_vz(emitter\_player) !\= 0\)   

 {  

     audio\_emitter\_velocity(emitter\_player, 0, 0, 0\);  

 }

The above code checks the current z velocity of a given emitter and if it is not equal to 0, it is set to 0\.
