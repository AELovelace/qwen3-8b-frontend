# layer\_sequence\_x

With this function you can set the position along the X (horizontal) axis of the room for the given sequence element. You supply the sequence element ID as returned by [layer\_sequence\_create()](layer_sequence_create.md) or by one of the [layer element functions](../General_Layer_Functions/General_Layer_Functions.md) along with the X position to set and the sequence will be moved to the new position.

 

#### Syntax:

layer\_sequence\_x(sequence\_element\_id, pos\_x)

| Argument | Type | Description |
| --- | --- | --- |
| sequence\_element\_id |  | The unique ID value of the sequence element to target |
| pos\_x |  | The X position to move the sequence element to |

 

#### Returns:

 

#### Example:

if (layer\_sequence\_exists(my\_seq))   

 {  

     layer\_sequence\_x(my\_seq, x);  

     layer\_sequence\_y(my\_seq, y);  

 }

The above code checks to see if the sequence element referenced in the variable "my\_seq" exists, and if it does it sets the x/y position to the that of the instance running the code.
