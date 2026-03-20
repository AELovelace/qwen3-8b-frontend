# draw\_ellipse

With this function you can draw either an outline of an ellipse or a filled ellipse by defining a rectangular area that will then have the ellipse created to fit. You can define how precise the drawing is with the function [draw\_set\_circle\_precision()](draw_set_circle_precision.md).

 
 

#### Syntax:

draw\_ellipse(x1, y1, x2, y2, outline)

| Argument | Type | Description |
| --- | --- | --- |
| x1 | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The x coordinate of the left of the ellipse. |
| y1 | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The y coordinate of the top of the ellipse. |
| x2 | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The x coordinate of the right of the ellipse. |
| y2 | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The y coordinate of the bottom of the ellipse. |
| outline | [Boolean](GameMaker_Language/GML_Overview/Data_Types.md) | Whether the ellipse is drawn filled (false) or as a one pixel wide outline (true). |

 

#### Returns:

N/A

 

#### Example:

draw\_set\_colour(c\_white);  

 draw\_ellipse(100, 100, 300, 200, false);

This will draw a filled ellipse within the defined rectangular area.
