# point\_direction

This function returns the direction of a vector formed by the specified components (x1, y1\) and (x2, y2\) in relation to the fixed x/y coordinates of the room.

For example, in the image below if we want to get the direction from the player ship position to the enemy position so that we can fire a missile at the enemy then we would use this function (the exact code is in the example below the image):

 

#### **Syntax:**

point\_direction(x1, y1, x2, y2\)

| Argument | Type | Description |
| --- | --- | --- |
| x1 | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate of the first component of the vector |
| y1 | [Real](../../../GML_Overview/Data_Types.md) | The y coordinate of the first component of the vector |
| x2 | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate of the second component of the vector |
| y2 | [Real](../../../GML_Overview/Data_Types.md) | The y coordinate of the second component of the vector |

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

var \_nearest \= instance\_nearest(x, y, obj\_enemy);  

 var \_ex \= \_nearest.x;  

 var \_ey \= \_nearest.y;  

 with (instance\_create\_layer(x, y, "Bullets", obj\_missile))  

 {  

     direction \= point\_direction(x, y, \_ex, \_ey);  

 }

The above code will get the x and y coordinates of the nearest enemy and then pass them to an instance of a bullet object to use in the point\_direction function to set its direction of travel correctly.
