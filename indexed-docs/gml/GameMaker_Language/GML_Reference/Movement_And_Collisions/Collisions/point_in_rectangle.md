# point\_in\_rectangle

This function checks if the given point falls within the given rectangular area. If the point falls within the defined rectangle the function will return true, otherwise the function will return false.

 

#### Syntax:

point\_in\_rectangle(px, py, x1, y1, x2, y2\)

| Argument | Type | Description |
| --- | --- | --- |
| px | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate of the point to check |
| py | [Real](../../../GML_Overview/Data_Types.md) | The y coordinate of the point to check |
| x1 | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate of the left side of the rectangle to check |
| y1 | [Real](../../../GML_Overview/Data_Types.md) | The y coordinate of the top side of the rectangle to check |
| x2 | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate of the right side of the rectangle to check |
| y2 | [Real](../../../GML_Overview/Data_Types.md) | The y coordinate of the bottom side of the rectangle to check |

 

#### Returns:

[Boolean](../../../GML_Overview/Data_Types.md)

 

#### Example:

if (point\_in\_rectangle(mouse\_x, mouse\_y, x \-10, y \- 10, x \+ 10, y \+ 10\))  

 {  

     audio\_play\_sound(snd\_click, 0, false);  

 }

This short code checks the mouse position against the defined rectangular area and plays a sound if it falls within the bounds.
