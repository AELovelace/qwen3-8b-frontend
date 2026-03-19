# draw\_line\_width\_colour

With this function you can draw a line of a specific width with the colour blended between colour 1 at the first point and colour 2 at the second point. The colour settings will over\-ride the base colour set with the function [draw\_set\_colour()](../Colour_And_Alpha/draw_set_colour.md). Please note that the line being drawn may need different values (\+/\-1 on the x, y) to be drawn with the desired dimensions due to differences across the various supported platforms.

 
 

#### Syntax:

draw\_line\_width\_colour(x1, y1, x2, y2, w, col1, col2\)

| Argument | Type | Description |
| --- | --- | --- |
| x1 | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The x coordinate of the start of the line. |
| y1 | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The y coordinate of the start of the line. |
| x2 | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The x coordinate of the end of the line. |
| y2 | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The y coordinate of the end of the line. |
| w | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The width in pixels of the line. |
| col1 | [Colour](GameMaker_Language/GML_Reference/Drawing/Colour_And_Alpha/Colour_And_Alpha.md) | The colour of the start of the line. |
| col2 | [Colour](GameMaker_Language/GML_Reference/Drawing/Colour_And_Alpha/Colour_And_Alpha.md) | The colour of the end of the line. |

 

#### Returns:

N/A

 

#### Example:

draw\_line\_width\_colour(50, 50, 300, 50, 4, c\_red, c\_blue);

This would draw a horizontal line from (50,50\) to (300,50\), four pixels wide, with a smooth red to blue gradient.
