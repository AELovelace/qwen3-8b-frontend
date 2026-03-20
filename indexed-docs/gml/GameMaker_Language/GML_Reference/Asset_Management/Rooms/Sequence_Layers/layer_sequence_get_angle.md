# layer\_sequence\_get\_angle

This function returns the current angle of the given sequence element in the game room.

You supply the sequence element ID \- as returned by [layer\_sequence\_create](layer_sequence_create.md) or by one of the [layer element functions](../General_Layer_Functions/General_Layer_Functions.md) \- and the function will return its current angle in the game room.

  Angles are returned in degrees, and 0º is to the right, 90º is up, 180º is to the left and 270º is down.

 

#### Syntax:

layer\_sequence\_get\_angle(sequence\_element\_id)

| Argument | Type | Description |
| --- | --- | --- |
| sequence\_element\_id | [Sequence Element ID](layer_sequence_create.md) | The unique ID value of the sequence element to target |

 

#### Returns:

[Real](../../../../GML_Overview/Data_Types.md)

 

#### Example:

var \_ang \= layer\_sequence\_get\_angle(title\_sequence);  

 if (\_ang \> 0\)  

 {  

     \_ang \-\= 1;  

     layer\_sequence\_angle(title\_sequence, \_ang);  

 }

The above code retrieves the current angle of the sequence element with the ID stored in the variable title\_sequence, and if it's not greater than 0, then 1 is subtracted form the current angle.
