# layer\_y

You can use this function to set the y position of the layer within the currently scoped room.

You supply the layer handle (which you get when you create the layer using [layer\_create](layer_create.md)) or the layer name (as a string \- this will have a performance impact) and the function will move the layer the given number of pixels along the vertical axis of the room.

 
 
 

#### Syntax:

layer\_y(layer\_id, y)

| Argument | Type | Description |
| --- | --- | --- |
| layer\_id | [String](../../../../GML_Overview/Data_Types.md) or [Layer](layer_get_id.md) | The handle of the layer to set the y position of |
| y | [Real](../../../../GML_Overview/Data_Types.md) | The y position in the room to set the layer to |

 

#### Returns:

N/A

 

#### Example:

var lay\_id \= layer\_get\_id("Sprites");  

 if layer\_get\_x(lay\_id) !\= 0 \|\| layer\_get\_y(lay\_id) !\= 0  

 {  

     layer\_x(lay\_id, 0\);  

     layer\_y(lay\_id, 0\);  

 }

The above code checks the given layer position and if it is not set to (0, 0\) then it is set to that position.
