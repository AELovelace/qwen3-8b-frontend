# draw\_triangle\_colour

With this function you can draw either an outline of a triangle or a filled triangle. If it is filled you can define the individual colours for each corner point and if these colours are not the same, you will get a gradient effect from one to the other (the colour settings will over\-ride the base colour set with the function [draw\_set\_colour()](../Colour_And_Alpha/draw_set_colour.md)).

 
 

#### Syntax:

draw\_triangle\_colour(x1, y1, x2, y2, x3, y3, col1, col2, col3, outline)

| Argument | Type | Description |
| --- | --- | --- |
| x1 | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The x coordinate of the triangle's first corner. |
| y1 | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The y coordinate of the triangle's first corner. |
| x2 | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The x coordinate of the triangle's second corner. |
| y2 | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The y coordinate of the triangle's second corner. |
| x3 | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The x coordinate of the triangle's third corner. |
| y3 | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The y coordinate of the triangle's third corner. |
| col1 | [Colour](GameMaker_Language/GML_Reference/Drawing/Colour_And_Alpha/Colour_And_Alpha.md) | The colour of the first corner. |
| col2 | [Colour](GameMaker_Language/GML_Reference/Drawing/Colour_And_Alpha/Colour_And_Alpha.md) | The colour of the second corner. |
| col3 | [Colour](GameMaker_Language/GML_Reference/Drawing/Colour_And_Alpha/Colour_And_Alpha.md) | The colour of the third corner. |
| outline | [Boolean](GameMaker_Language/GML_Overview/Data_Types.md) | Whether the triangle is an outline (true) or filled in (false). |

 

#### Returns:

N/A

 

#### Example:

draw\_triangle\_colour(200, 200, 300, 200, 200, 300, c\_red, c\_blue, c\_blue, false);

This would draw a filled isosceles right\-angled triangle with red at the right angle, blue on the other two corners.
