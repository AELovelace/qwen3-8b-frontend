# layer\_sequence\_exists

With this function you can check to see if a sequence element exists on the given layer. You supply the layer handle which can be a string of the layer name \- as defined in the Room Editor \- or the unique layer handle \- as returned by the function [layer\_get\_id()](../General_Layer_Functions/layer_get_id.md), as well the sequence element ID \- as returned by [layer\_sequence\_create()](layer_sequence_create.md) or by one of the [layer element functions](../General_Layer_Functions/General_Layer_Functions.md) \- and it will return true if the given element exists or false otherwise.

 

#### Syntax:

layer\_sequence\_exists(layer\_id, sequence\_element\_id)

| Argument | Type | Description |
| --- | --- | --- |
| layer\_id | [String](../../../../GML_Overview/Data_Types.md) or [Layer](../General_Layer_Functions/layer_get_id.md) | The unique ID or name of the layer to check |
| sequence\_element\_id | [Sequence Element ID](layer_sequence_create.md) | The unique ID value of the sequence element to target |

 

#### Returns:

[Boolean](../../../../GML_Overview/Data_Types.md)

 

#### Example:

my\_seq \= layer\_get\_all\_elements("SequenceLayer")\[0];  

  

 if (!layer\_sequence\_exists("SequenceLayer", my\_seq))  

 {  

     my\_seq \= layer\_sequence\_create("SequenceLayer", 0, 0, seq\_AnimatedBackground);  

     layer\_sequence\_pause(my\_seq);  

 }
 

The above code gets all elements on a layer and stores its first element in a variable, which is assumed to be a sequence element. Then it checks to see if the sequence element exists, and if it does not then it creates a new sequence on the given layer and then pauses it.
