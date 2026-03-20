# layer\_sequence\_get\_yscale

This function returns the current scale along the y axis of the given sequence element in the game room.

You supply the sequence element ID \- as returned by [layer\_sequence\_create](layer_sequence_create.md) or by one of the [layer element functions](../General_Layer_Functions/General_Layer_Functions.md) \- and it will return the current scale along the y axis of the sequence element in the game room.

 

#### Syntax:

layer\_sequence\_get\_yscale(sequence\_element\_id)

| Argument | Type | Description |
| --- | --- | --- |
| sequence\_element\_id | [Sequence Element ID](layer_sequence_create.md) | The unique ID value of the sequence element to target |

 

#### Returns:

[Real](../../../../GML_Overview/Data_Types.md)

 

#### Example:

var \_ys \= layer\_sequence\_get\_yscale(title\_sequence);  

 if (\_ys \< 1\)  

 {  

     \_ys \+\= 0\.01;  

     layer\_sequence\_yscale(title\_sequence, \_ys);  

 }

The above code retrieves the current scale along the y axis of the sequence element with the ID stored in the variable title\_sequence, and if it's less than 1, then 0\.01 is added to the current Y scale.
