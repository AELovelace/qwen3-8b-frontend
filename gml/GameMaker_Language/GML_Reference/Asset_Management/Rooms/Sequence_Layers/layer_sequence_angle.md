# layer\_sequence\_angle

With this function you can set the angle of rotation for the given sequence element. You supply the sequence element ID as returned by [layer\_sequence\_create()](layer_sequence_create.md) or by one of the [layer element functions](../General_Layer_Functions/General_Layer_Functions.md) along with the new angle to set and the sequence will be rotated about its origin to the new position. Angles in GameMaker are calculated with 0º to the right, and go anti\-clockwise \- so 90º is up, 180º is left and 270º is down \- and the default angle for a sequence would be 0º.

 
 

#### Syntax:

layer\_sequence\_angle(sequence\_element\_id, angle)

| Argument | Type | Description |
| --- | --- | --- |
| sequence\_element\_id | [Sequence Element ID](layer_sequence_create.md) | The unique ID value of the sequence element to target |
| angle | [Real](../../../../GML_Overview/Data_Types.md) | The new angle to rotate the sequence element to |

 

#### Returns:

N/A

 

#### Example:

if (current\_angle \< 90\)  

 {  

     current\_angle \+\= 1;  

     layer\_sequence\_angle(my\_seq, current\_angle);  

 }

The above code checks the value held in the current\_angle variable, and if it is less than 90 then it adds to it then uses the value to set the angle of the sequence element referenced in the variable my\_seq.
