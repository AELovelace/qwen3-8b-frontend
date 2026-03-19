# distance\_to\_point

This function calculates the distance from the edge of the bounding box of the calling instance to the specified (x , y) position in the room, with the return value being in pixels.

  If the calling object has no sprite or mask defined, the results will be incorrect.

 

#### **Syntax:**

distance\_to\_point(x, y)

| Argument | Type | Description |
| --- | --- | --- |
| x | [Real](../../../GML_Overview/Data_Types.md) | The x position to check |
| y | [Real](../../../GML_Overview/Data_Types.md) | The y position to check |

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

if (distance\_to\_point(obj\_player.x, obj\_player.y) \< range)  

 {  

     can\_shoot \= true;  

 }

The above code will check for the distance to the player object x/y position and if it is less than the value stored in the variable range the variable can\_shoot is set to true.
