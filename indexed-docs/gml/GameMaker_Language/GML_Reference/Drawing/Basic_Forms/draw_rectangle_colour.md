# draw\_rectangle\_colour

With this function you can draw either an outline of a rectangle or a filled rectangle by defining an area where the (x1,y1\) position is the top left corner and the (x2,y2\) position is the bottom right corner. If it is filled you can define the individual colours for each corner point and if these colours are not the same, you will get a gradient effect from one to the other (the colour settings will over\-ride the base colour set with the function [draw\_set\_colour()](../Colour_And_Alpha/draw_set_colour.md)). Please note that the rectangle being drawn may need different values (\+/\-1 on the x, y, or width or height) to be drawn with the desired dimensions due to differences across the various supported platforms.

 
 

#### Syntax:

draw\_rectangle\_colour(x1, y1, x2, y2, col1, col2, col3, col4, outline)

| Argument | Type | Description |
| --- | --- | --- |
| x1 | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The x coordinate of the left of the rectangle. |
| y1 | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The y coordinate of the top of the rectangle. |
| x2 | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The x coordinate of the right of the rectangle. |
| y2 | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The y coordinate of the bottom of the rectangle. |
| col1 | [Colour](GameMaker_Language/GML_Reference/Drawing/Colour_And_Alpha/Colour_And_Alpha.md) | The colour of the top left corner. |
| col2 | [Colour](GameMaker_Language/GML_Reference/Drawing/Colour_And_Alpha/Colour_And_Alpha.md) | The colour of the top right corner. |
| col3 | [Colour](GameMaker_Language/GML_Reference/Drawing/Colour_And_Alpha/Colour_And_Alpha.md) | The colour of the bottom right corner. |
| col4 | [Colour](GameMaker_Language/GML_Reference/Drawing/Colour_And_Alpha/Colour_And_Alpha.md) | The colour of the bottom left corner. |
| outline | [Boolean](GameMaker_Language/GML_Overview/Data_Types.md) | Whether the rectangle is an outline (true) or filled in (false). |

 

#### Returns:

N/A

 

#### Example:

draw\_rectangle\_colour(50, 50, 200, 200, c\_black, c\_white, c\_black, c\_white, false);

This would draw a filled\-in square with a smooth black/white gradient between the corners.
