# layer\_sequence\_get\_length

This function returns the length of the sequence referenced by the given sequence element.

You supply the sequence element ID \- as returned by [layer\_sequence\_create](layer_sequence_create.md) or by one of the [layer element functions](../General_Layer_Functions/General_Layer_Functions.md) \- and the function will return the length of its sequence. This is the number of frames that the sequence will run for.

 

#### Syntax:

layer\_sequence\_get\_length(sequence\_element\_id)

| Argument | Type | Description |
| --- | --- | --- |
| sequence\_element\_id | [Sequence Element ID](layer_sequence_create.md) | The unique ID value of the sequence element to target |

 

#### Returns:

[Real](../../../../GML_Overview/Data_Types.md)

 

#### Example:

var \_frames \= layer\_sequence\_get\_length(my\_seq);  

 alarm\[0] \= \_frames;

The above code retrieves the number of frames that a sequence will run, then uses this value to set an alarm.
