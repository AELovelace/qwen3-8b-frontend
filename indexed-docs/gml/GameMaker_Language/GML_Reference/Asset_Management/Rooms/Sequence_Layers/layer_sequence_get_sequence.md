# layer\_sequence\_get\_sequence

This function gets the sequence object referenced by the given sequence element.

You supply the sequence element ID \- as returned by [layer\_sequence\_create](layer_sequence_create.md) or by one of the [layer element functions](../General_Layer_Functions/General_Layer_Functions.md) \- and the function will return its sequence object [struct](../../../../GML_Overview/Structs.md). This function bypasses the need to first get the sequence instance struct and permits you to access the sequence data directly.

You can find out more about the format of the sequence object struct on [The Sequence Object Struct](../../Sequences/Sequence_Structs/The_Sequence_Object_Struct.md) page.

 

#### Syntax:

layer\_sequence\_get\_sequence(sequence\_element\_id)

| Argument | Type | Description |
| --- | --- | --- |
| sequence\_element\_id | [Sequence Element ID](layer_sequence_create.md) | The unique ID value of the sequence element to target |

 

#### Returns:

[Sequence Object Struct](../../Sequences/Sequence_Structs/The_Sequence_Object_Struct.md)

 

#### Example:

var \_seq \= layer\_sequence\_create("Background", 0, 0, seq\_AnimatedBackground);  

 var \_struct \= layer\_sequence\_get\_sequence(\_seq);  

 \_struct.playbackSpeedType \= spritespeed\_framespersecond;  

 \_struct.playbackSpeed \= 30;

The above code creates a new sequence element and then retrieves its sequence data struct. This is then used to change the playback speed and type of the sequence.
