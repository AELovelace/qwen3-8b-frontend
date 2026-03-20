# audio\_emitter\_get\_x

This function returns the current x position of the given audio emitter.

 

#### Syntax:

audio\_emitter\_get\_x(emitter)

| Argument | Type | Description |
| --- | --- | --- |
| emitter | Audio Emitter ID | The index of the emitter to use. |

 

#### Returns:

Real

 

#### Example:

if (audio\_emitter\_get\_x(emitter\_player) !\= x)   

 {  

     audio\_emitter\_position(emitter\_player, x, y, 0\);  

 }

The above code checks the current x position of a given emitter and if it is not equal to the instance x position, it is set to the instance position.
