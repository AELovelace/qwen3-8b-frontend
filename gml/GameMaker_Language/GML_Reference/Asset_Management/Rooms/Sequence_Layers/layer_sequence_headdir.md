# layer\_sequence\_headdir

With this function you can set the direction for the given sequence [playhead](#). You supply the sequence element ID as returned by [layer\_sequence\_create](layer_sequence_create.md) or by one of the [layer element functions](../General_Layer_Functions/General_Layer_Functions.md), and then give the playhead direction which should be one of the following constants:

 
 

#### Syntax:

layer\_sequence\_headdir(sequence\_element\_id, direction)

| Argument | Type | Description |
| --- | --- | --- |
| sequence\_element\_id | [Sequence Element ID](../../../../../../GameMaker_Language/GML_Reference/Asset_Management/Rooms/Sequence_Layers/layer_sequence_create.md) | The unique ID value of the sequence element to target |
| direction | [Sequence Direction Constant](../../../../../../GameMaker_Language/GML_Reference/Asset_Management/Sequences/Sequence_Structs/The_Sequence_Instance_Struct.md) | The playhead direction, a constant, listed above |

 

#### Returns:

N/A

 

#### Example:

var \_seq \= layer\_sequence\_create("Background", 0, 0, seq\_AnimatedBackground);  

layer\_sequence\_headdir(\_seq, seqdir\_left);
 

The above code creates a new sequence and stores its ID in a local variable \_seq. This ID is then used to set the playhead direction to decrement frames (right to left playback).
