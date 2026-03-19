# layer\_sequence\_y

With this function you can set the position along the Y (vertical) axis of the room for the given sequence element. You supply the sequence element ID as returned by [layer\_sequence\_create()](layer_sequence_create.md) or by one of the [layer element functions](../General_Layer_Functions/General_Layer_Functions.md) along with the Y position to set and the sequence will be moved to the new position.

 

#### Syntax:

layer\_sequence\_y(sequence\_element\_id, pos\_y)

| Argument | Type | Description |
| --- | --- | --- |
| sequence\_element\_id |  | The unique ID value of the sequence element to target |
| pos\_y |  | The Y position to move the sequence element to |

 

#### Returns:

 

#### Example:

if (layer\_sequence\_exists(my\_seq))   

 {  

     layer\_sequence\_x(my\_seq, x);  

     layer\_sequence\_y(my\_seq, y);  

 }

The above code checks to see if the sequence element referenced in the variable "my\_seq" exists, and if it does it sets the x/y position to the that of the instance running the code.
