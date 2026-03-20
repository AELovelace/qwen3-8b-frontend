# layer\_sequence\_get\_headpos

This function returns the current [playhead](#) position (the current frame the playhead is on) of the given sequence element.

You supply the sequence element ID \- as returned by [layer\_sequence\_create](layer_sequence_create.md) or by one of the [layer element functions](../General_Layer_Functions/General_Layer_Functions.md) \- and the function will return its current [playhead](#) position.

 

#### Syntax:

layer\_sequence\_get\_headpos(sequence\_element\_id)

| Argument | Type | Description |
| --- | --- | --- |
| sequence\_element\_id | [Sequence Element ID](layer_sequence_create.md) | The unique ID value of the sequence element to target |

 

#### Returns:

[Real](../../../../GML_Overview/Data_Types.md)

 

#### Example:

if (layer\_sequence\_get\_headpos(title\_sequence) !\= 0\)  

 {  

     layer\_sequence\_headpos(title\_sequence, 0\);  

 }

The above code checks the current playhead position of the sequence element ID stored in the variable title\_sequence, and if it's not set to 0, it is set to this value.
