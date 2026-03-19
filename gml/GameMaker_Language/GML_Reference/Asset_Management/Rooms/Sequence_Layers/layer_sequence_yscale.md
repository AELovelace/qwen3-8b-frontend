# layer\_sequence\_yscale

With this function you can set the Y scale for the given sequence element. You supply the sequence element ID as returned by [layer\_sequence\_create()](layer_sequence_create.md) or by one of the [layer element functions](../General_Layer_Functions/General_Layer_Functions.md) along with the new scale to set on the Y axis and the sequence will be scaled by this amount. A scale of 1 indicates no scaling (1:1\), smaller values will scale down (0\.5, for example, will half the width of the sequence), larger values will scale up and negative values will flip the sequence about its origin *and* scale it unless the value used is exactly \-1 (in which case the sequence is just flipped about its origin with no scaling).

It is very important to note that applying *uneven* scaling (eg: scaling the X axis by 3 and the Y axis by 2\) to sequence elements that contain any instance which uses *rotation*, **may cause issues with the instance drawing, collisions, culling, and many other things**. Basically, if your sequence relies on *any* instance properties then we do not recommend that you combine uneven scaling along with instance rotation.

 
 

#### Syntax:

layer\_sequence\_yscale(sequence\_element\_id, xscale)

| Argument | Type | Description |
| --- | --- | --- |
| sequence\_element\_id | [Sequence Element ID](layer_sequence_create.md) | The unique ID value of the sequence element to target |
| yscale | [Real](../../../../GML_Overview/Data_Types.md) | The new Y axis scale value to apply to the sequence element |

 

#### Returns:

N/A

 

#### Example:

if (seq\_scale \< 2\)  

 {  

     seq\_scale \+\= 0\.01;  

     layer\_sequence\_xscale(my\_seq, seq\_scale);  

     layer\_sequence\_yscale(my\_seq, seq\_scale);  

 }

The above code checks the value held in the seq\_scale variable, and if it is less than 2 then it adds to it then uses the value to set the X and Y scale of the sequence element referenced in the variable my\_seq.
