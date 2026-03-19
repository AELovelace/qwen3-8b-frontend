# draw\_circle

With this function you can draw either an outline of a circle or a filled circle. You can define how precise the drawing is with the function [draw\_set\_circle\_precision()](draw_set_circle_precision.md).

 
 

#### Syntax:

draw\_circle(x, y, r, outline)

| Argument | Type | Description |
| --- | --- | --- |
| x | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The x coordinate of the center of the circle. |
| y | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The y coordinate of the center of the circle. |
| r | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The circle's radius (length from its center to its edge) |
| outline | [Boolean](GameMaker_Language/GML_Overview/Data_Types.md) | Whether the circle is drawn filled (false) or as a one pixel wide outline (true). |

 

#### Returns:

N/A

 

#### Example:

draw\_set\_colour(c\_white);  

 draw\_circle(100, 100, 50, true);

This will draw a one pixel wide white circle outline with a radius of 50 pixels.
