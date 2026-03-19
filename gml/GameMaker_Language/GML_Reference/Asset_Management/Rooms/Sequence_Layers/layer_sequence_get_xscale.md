# layer\_sequence\_get\_xscale

This function returns the current scale along the x axis of the given sequence element in the game room.

You supply the sequence element ID \- as returned by [layer\_sequence\_create](layer_sequence_create.md) or by one of the [layer element functions](../General_Layer_Functions/General_Layer_Functions.md) \- and it will return the current scale along the x axis of the sequence element in the game room.

 

#### Syntax:

layer\_sequence\_get\_xscale(sequence\_element\_id)

| Argument | Type | Description |
| --- | --- | --- |
| sequence\_element\_id | [Sequence Element ID](layer_sequence_create.md) | The unique ID value of the sequence element to target |

 

#### Returns:

[Real](../../../../GML_Overview/Data_Types.md)

 

#### Example:

var \_xs \= layer\_sequence\_get\_xscale(title\_sequence)  

 if (\_xs \< 1\)  

 {  

     \_xs \+\= 0\.01;  

     layer\_sequence\_xscale(title\_sequence, \_xs);  

 }

The above code retrieves the current scale along the X axis of the sequence element with the ID stored in the variable title\_sequence, and if it's less than 1, then 0\.01 is added to the current x scale.
