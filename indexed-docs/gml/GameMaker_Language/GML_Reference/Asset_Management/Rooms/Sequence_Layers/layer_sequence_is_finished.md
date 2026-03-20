# layer\_sequence\_is\_finished

This function returns whether the given sequence has finished playing.

You supply the sequence element ID \- as returned by [layer\_sequence\_create](layer_sequence_create.md) or by one of the [layer element functions](../General_Layer_Functions/General_Layer_Functions.md) \- and it will check if the sequence has finished playing or not, returning true if it has, false if it hasn't.

  This is only applicable when the sequence is *not* set to loop or ping\-pong in the playback mode.

 

#### Syntax:

layer\_sequence\_is\_finished(sequence\_element\_id)

| Argument | Type | Description |
| --- | --- | --- |
| sequence\_element\_id | [Sequence Element ID](layer_sequence_create.md) | The unique ID value of the sequence element to target |

 

#### Returns:

[Boolean](../../../../GML_Overview/Data_Types.md)

 

#### Example:

if (layer\_sequence\_is\_finished(title\_sequence) !\= 0\)  

 {  

     alarm\[0] \= game\_get\_speed(gamespeed\_fps) \* 3;  

     layer\_sequence\_play(title\_sequence);  

 }

The above code checks if the sequence element ID stored in the variable title\_sequence is finished, and if it is it starts playing it again and sets an alarm.
