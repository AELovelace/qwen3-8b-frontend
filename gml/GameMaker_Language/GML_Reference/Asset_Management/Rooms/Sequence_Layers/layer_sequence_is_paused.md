# layer\_sequence\_is\_paused

This function returns whether the given sequence is currently paused.

You supply the sequence element ID \- as returned by [layer\_sequence\_create](layer_sequence_create.md) or by one of the [layer element functions](../General_Layer_Functions/General_Layer_Functions.md) \- and it will check if the sequence is currently paused or not, returning true if it is paused, false if it isn't.

 

#### Syntax:

layer\_sequence\_is\_paused(sequence\_element\_id)

| Argument | Type | Description |
| --- | --- | --- |
| sequence\_element\_id | [Sequence Element ID](layer_sequence_create.md) | The unique ID value of the sequence element to target |

 

#### Returns:

[Boolean](../../../../GML_Overview/Data_Types.md)

 

#### Example:

if (layer\_sequence\_is\_paused(title\_sequence) !\= 0\)  

 {  

     layer\_sequence\_play(title\_sequence);  

 }

The above code checks if the sequence element ID stored in the variable title\_sequence is paused, and if it is it, resumes it.
