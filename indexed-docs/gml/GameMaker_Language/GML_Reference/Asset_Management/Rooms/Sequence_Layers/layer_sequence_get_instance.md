# layer\_sequence\_get\_instance

This function returns the sequence *instance* [struct](../../../../GML_Overview/Structs.md) for the given sequence element.

You supply the sequence element ID \- as returned by [layer\_sequence\_create](layer_sequence_create.md) or by one of the [layer element functions](../General_Layer_Functions/General_Layer_Functions.md) \- and the function will return its sequence *instance* [struct](../../../../GML_Overview/Structs.md).

You can find out more about the format of the sequence instance struct on [The Sequence Instance Struct](../../Sequences/Sequence_Structs/The_Sequence_Instance_Struct.md) page.

 

#### Syntax:

layer\_sequence\_get\_instance(sequence\_element\_id)

| Argument | Type | Description |
| --- | --- | --- |
| sequence\_element\_id | [Sequence Element ID](layer_sequence_create.md) | The unique ID value of the sequence element to target |

 

#### Returns:

[Sequence Instance Struct](../../Sequences/Sequence_Structs/The_Sequence_Instance_Struct.md)

 

#### Example:

var \_seq \= layer\_sequence\_create("Background", 0, 0, seq\_AnimatedBackground);  

 var \_struct \= layer\_sequence\_get\_instance(\_seq);  

 \_struct.speedScale \= 0\.5;

The above code creates a new sequence element and then retrieves its sequence instance ID. This is then used to change the playback speed scale property of the sequence instance.
