# draw\_ellipse\_colour

With this function you can draw either an outline of an ellipse or a filled ellipse by defining a rectangular area that will then have the ellipse created to fit. If it is filled you can define the interior and exterior fill colours. If these colours are not the same, you will get a gradient effect from one to the other (the colour settings will over\-ride the base colour set with the function [draw\_set\_colour()](../Colour_And_Alpha/draw_set_colour.md)). You can define how precise the drawing is with the function [draw\_set\_circle\_precision()](draw_set_circle_precision.md).

 
 

#### Syntax:

draw\_ellipse\_colour(x1, y1, x2, y2, col1, col2, outline)

| Argument | Type | Description |
| --- | --- | --- |
| x1 | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The x coordinate of the left of the ellipse. |
| y1 | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The y coordinate of the top of the ellipse. |
| x2 | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The x coordinate of the right of the ellipse. |
| y2 | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The y coordinate of the bottom of the ellipse. |
| col1 | [Colour](GameMaker_Language/GML_Reference/Drawing/Colour_And_Alpha/Colour_And_Alpha.md) | The colour of the center. |
| col2 | [Colour](GameMaker_Language/GML_Reference/Drawing/Colour_And_Alpha/Colour_And_Alpha.md) | The colour of the edge. |
| outline | [Boolean](GameMaker_Language/GML_Overview/Data_Types.md) | Whether the ellipse is an outline (true) or filled in (false). |

 

#### Returns:

N/A

 

#### Example:

draw\_ellipse\_colour(50, 50, 200, 100, c\_black, c\_white, false);

This would draw a filled\-in, horizontally\-stretched ellipse with a black center and white edge.
