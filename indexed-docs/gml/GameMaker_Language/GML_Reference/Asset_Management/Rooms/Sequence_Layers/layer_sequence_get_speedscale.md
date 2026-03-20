# layer\_sequence\_get\_speedscale

This function returns the current playback speed scale of the given sequence element.

You supply the sequence element ID \- as returned by [layer\_sequence\_create](layer_sequence_create.md) or by one of the [layer element functions](../General_Layer_Functions/General_Layer_Functions.md) \- and the will return its current playback speed scale. This is the *multiplier* value used to slow down or speed up the playback speed. A value of 1 is the default value, and values lower than 1 mean that playback is slowed down and values greater than 1 mean that playback is sped up.

 

#### Syntax:

layer\_sequence\_get\_speedscale(sequence\_element\_id)

| Argument | Type | Description |
| --- | --- | --- |
| sequence\_element\_id | [Sequence Element ID](layer_sequence_create.md) | The unique ID value of the sequence element to target |

 

#### Returns:

[Real](../../../../GML_Overview/Data_Types.md)

 

#### Example:

if (layer\_sequence\_get\_speedscale(title\_sequence) !\= 1\)  

 {  

     layer\_sequence\_speedscale(title\_sequence, 1\);  

 }

The above code checks the current playhead speed scale of the sequence element ID stored in the variable title\_sequence, and if it's not set to 1 it is set to this value.
