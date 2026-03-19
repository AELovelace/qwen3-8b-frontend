# point\_in\_circle

This function checks if the given point falls within the given circular area. If the point falls within the defined circle the function will return true, otherwise the function will return false.

 

#### Syntax:

point\_in\_circle(px, py, x1, y1, rad)

| Argument | Type | Description |
| --- | --- | --- |
| px | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate of the point to check |
| py | [Real](../../../GML_Overview/Data_Types.md) | The y coordinate of the point to check |
| x1 | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate of the circle centre |
| y1 | [Real](../../../GML_Overview/Data_Types.md) | The y coordinate of the circle centre |
| rad | [Real](../../../GML_Overview/Data_Types.md) | The radius of the circle |

 

#### Returns:

[Boolean](../../../GML_Overview/Data_Types.md)

 

#### Example:

if (point\_in\_circle(mouse\_x, mouse\_y, x, y, 16\))  

 {  

     over \= true;  

 }  

 else  

 {  

     over \= false;  

 }

The above code uses the point\_in\_circle function to check if the mouse position falls within the defined circular area, setting the variable over to true if it does, or false otherwise.
