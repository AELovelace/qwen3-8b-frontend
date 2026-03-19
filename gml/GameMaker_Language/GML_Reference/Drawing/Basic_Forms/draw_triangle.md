# draw\_triangle

With this function you can draw either an outline of a triangle or a filled triangle.

 
 

#### Syntax:

draw\_triangle(x1, y1, x2, y2, x3, y3, outline)

| Argument | Type | Description |
| --- | --- | --- |
| x1 | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The x coordinate of the triangle's first corner. |
| y1 | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The y coordinate of the triangle's first corner. |
| x2 | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The x coordinate of the triangle's second corner. |
| y2 | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The y coordinate of the triangle's second corner. |
| x3 | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The x coordinate of the triangle's third corner. |
| y3 | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The y coordinate of the triangle's third corner. |
| outline | [Boolean](GameMaker_Language/GML_Overview/Data_Types.md) | Whether the triangle is drawn filled (false) or as a one pixel wide outline (true). |

 

#### Returns:

N/A

 

#### Example:

draw\_set\_colour(c\_aqua);  

 draw\_triangle(50, 50, 200, 50, 50, 200, 0\);

This will draw a filled aquamarine\-coloured isosceles right\-angled triangle, with its first corner at (50,50\), its second at (200,50\) and its third at (50,200\).
