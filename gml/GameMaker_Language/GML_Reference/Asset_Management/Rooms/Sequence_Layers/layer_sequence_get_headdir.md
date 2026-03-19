# layer\_sequence\_get\_headdir

This function returns the current [playhead](#) direction of the given sequence element.

You supply the sequence element ID \- as returned by [layer\_sequence\_create](layer_sequence_create.md) or by one of the [layer element functions](../General_Layer_Functions/General_Layer_Functions.md) \- and the function will return its current [playhead](#) direction, which will be one of the constants listed below.

 
 

#### Syntax:

layer\_sequence\_get\_headdir(sequence\_element\_id)

| Argument | Type | Description |
| --- | --- | --- |
| sequence\_element\_id | [Sequence Element ID](layer_sequence_create.md) | The unique ID value of the sequence element to target |

 

#### Returns:

[Constant](../../../../GML_Overview/Variables/Constants.md)

 

#### Example:

if (layer\_sequence\_get\_headdir(title\_sequence) !\= seqdir\_left)  

 {  

     layer\_sequence\_headdir(title\_sequence, seqdir\_left);  

 }

The above code checks the current playhead direction of the sequence element ID stored in the variable title\_sequence, and if it's not set to seqdir\_left, it is set to this value.
