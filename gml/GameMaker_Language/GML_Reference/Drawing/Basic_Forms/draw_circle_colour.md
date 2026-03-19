# draw\_circle\_colour

With this function you can draw either an outline of a circle or a filled circle, and if it is filled you can define the interior and exterior fill colours. If these colours are not the same, you will get a gradient effect from one to the other and the colour settings will over\-ride the base colour set with the function [draw\_set\_colour()](../Colour_And_Alpha/draw_set_colour.md). You can define how precise the drawing is with the function [draw\_set\_circle\_precision()](draw_set_circle_precision.md).

 
 

#### Syntax:

draw\_circle\_colour(x, y, r, col1, col2, outline)

| Argument | Type | Description |
| --- | --- | --- |
| x | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The x coordinate of the center of the circle. |
| y | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The y coordinate of the center of the circle. |
| r | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The radius (distance from center to edge) of the circle in pixels. |
| col1 | [Colour](GameMaker_Language/GML_Reference/Drawing/Colour_And_Alpha/Colour_And_Alpha.md) | The colour at the center of the circle. |
| col2 | [Colour](GameMaker_Language/GML_Reference/Drawing/Colour_And_Alpha/Colour_And_Alpha.md) | The colour at the edge of the circle. |
| outline | [Boolean](GameMaker_Language/GML_Overview/Data_Types.md) | Whether the circle is an outline (true) or not (false). If true, col1 is irrelevant. |

 

#### Returns:

N/A

 

#### Example:

draw\_circle\_colour(x, y, 100, c\_white, c\_black, false);

This would draw a filled circle with its center at the executing instance's x and y position, with a radius of 100 pixels, from white in the center to black at the outside.
