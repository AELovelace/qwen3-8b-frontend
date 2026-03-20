# layer\_sequence\_get\_x

This function returns the current x position in the game room for the given sequence element.

You supply the sequence element ID \- as returned by [layer\_sequence\_create](layer_sequence_create.md) or by one of the [layer element functions](../General_Layer_Functions/General_Layer_Functions.md) \- and it will return the current x position in the game room for the sequence.

 

#### Syntax:

layer\_sequence\_get\_x(sequence\_element\_id)

| Argument | Type | Description |
| --- | --- | --- |
| sequence\_element\_id | [Sequence Element ID](layer_sequence_create.md) | The unique ID value of the sequence element to target |

 

#### Returns:

[Real](../../../../GML_Overview/Data_Types.md)

 

#### Example:

if (layer\_sequence\_get\_x(title\_sequence) !\= room\_width / 2\)  

 {  

     layer\_sequence\_x(title\_sequence, room\_width / 2\);  

 }

The above code checks the X position of the sequence element ID stored in the variable title\_sequence, and if it's not set to half the room width, it is set to this value.
