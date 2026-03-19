# audio\_emitter\_get\_z

This function returns the current z position of the given audio emitter.

 

#### Syntax:

audio\_emitter\_get\_z(emitter)

| Argument | Type | Description |
| --- | --- | --- |
| emitter | Audio Emitter ID | The index of the emitter to use. |

 

#### Returns:

Real

 

#### Example:

if (audio\_emitter\_get\_z(emitter\_player) !\= 0\)   

 {  

     var ex \= audio\_emitter\_get\_x(emitter\_player);  

     var ey \= audio\_emitter\_get\_y(emitter\_player);  

     audio\_emitter\_position(emitter\_player, ex, ey, 0\);  

 }

The above code checks the current z position of a given emitter and if it is not equal to 0, it is set to 0\.
