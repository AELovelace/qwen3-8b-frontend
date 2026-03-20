# rectangle\_in\_triangle

This function will check a rectangular area that you define to see if it is either not in collision, completely within the destination bounds, or if it is simply touching, a defined triangular area. If they are not touching at all the function will return 0, if the source is completely within the destination it will return 1, and if they are simply overlapping then it will return 2\.

The image below illustrates this:

#### Syntax:

rectangle\_in\_triangle(sx1, sy1, sx2, sy2, dx1, dy1, dx2, dy2, dx3, dy3\)

| Argument | Type | Description |
| --- | --- | --- |
| sx1 | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate of the left side of the source rectangle |
| sy1 | [Real](../../../GML_Overview/Data_Types.md) | The y coordinate of the top side of the source rectangle |
| sx2 | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate of the right side of the source rectangle |
| sy2 | [Real](../../../GML_Overview/Data_Types.md) | The y coordinate of the bottom side of the source rectangle |
| x1 | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate of the first side of the triangle to check |
| y1 | [Real](../../../GML_Overview/Data_Types.md) | The y coordinate of the first side of the triangle to check |
| x2 | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate of the second side of the triangle to check |
| y2 | [Real](../../../GML_Overview/Data_Types.md) | The y coordinate of the second side of the triangle to check |
| x3 | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate of the third side of the triangle to check |
| y3 | [Real](../../../GML_Overview/Data_Types.md) | The y coordinate of the third side of the triangle to check |

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

var \_inst \= instance\_nearest(x, y, obj\_player);  

 if (instance\_exists(\_inst))  

 {  

     var \_x1 \= x \+ lengthdir\_x(100, image\_angle \- 45\);  

     var \_y1 \= y \+ lengthdir\_y(100, image\_angle \- 45\);  

     var \_x2 \= x \+ lengthdir\_x(100, image\_angle \+ 45\);  

     var \_y2 \= y \+ lengthdir\_y(100, image\_angle \+ 45\);  

     if (rectangle\_in\_triangle(\_inst.bbox\_left, \_inst.bbox\_top, \_inst.bbox\_right, \_inst.bbox\_bottom, x, y, \_x1, \_y1, \_x2, \_y2\) \=\= 1\)  

     {  

         can\_see \= true;  

     }  

 }

The above code uses the rectangle\_in\_triangle function as a "cone of vision" to check for an instance of obj\_player. If the full bounding box is within the given triangular area, it will set a variable to true.
