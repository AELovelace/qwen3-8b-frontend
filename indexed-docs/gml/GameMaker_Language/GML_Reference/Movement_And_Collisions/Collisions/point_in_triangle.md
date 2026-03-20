# point\_in\_triangle

This function checks if the given point falls within the given triangular area. If the point falls within the defined triangle the function will return true, otherwise the function will return false.

 

#### Syntax:

point\_in\_triangle(px, py, x1, y1, x2, y2, x3, y3\)

| Argument | Type | Description |
| --- | --- | --- |
| px | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate of the point to check |
| py | [Real](../../../GML_Overview/Data_Types.md) | The y coordinate of the point to check |
| x1 | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate of the first corner of the triangle to check |
| y1 | [Real](../../../GML_Overview/Data_Types.md) | The y coordinate of the first corner of the triangle to check |
| x2 | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate of the second corner of the triangle to check |
| y2 | [Real](../../../GML_Overview/Data_Types.md) | The y coordinate of the second corner of the triangle to check |
| x3 | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate of the third corner of the triangle to check |
| y3 | [Real](../../../GML_Overview/Data_Types.md) | The y coordinate of the third corner of the triangle to check |

 

#### Returns:

[Boolean](../../../GML_Overview/Data_Types.md)

 

#### Example:

var \_inst \= instance\_nearest(x, y, obj\_player);  

 var \_can\_see \= false;  

 if (instance\_exists(\_inst))  

 {  

     var \_x1 \= x \+ lengthdir\_x(100, image\_angle \- 45\);  

     var \_y1 \= y \+ lengthdir\_y(100, image\_angle \- 45\);  

     var \_x2 \= x \+ lengthdir\_x(100, image\_angle \+ 45\);  

     var \_y2 \= y \+ lengthdir\_y(100, image\_angle \+ 45\);  

     \_can\_see \= point\_in\_triangle(\_inst.x, \_inst.y, x, y, \_x1, \_y1, \_x2, \_y2\);  

 }

The above code uses the point\_in\_triangle function as a "cone of vision" to check for an instance of obj\_player and assigns the return value to a variable \_can\_see.
