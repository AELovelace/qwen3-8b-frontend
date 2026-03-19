# draw\_roundrect\_colour\_ext

With this function you can draw either an outline of a rounded rectangle or a filled rounded rectangle where the (x1,y1\) position is the top left corner and the (x2,y2\) position is the bottom right corner. If the rectangle is filled, then the colour arguments will be used to generate a colour gradient from the centre to the edges, where colour 1 is the centre colour and colour 2 the edge colour. You must also supply radius values for the x and y axis (in pixels) and the corners will be rounded by these amounts. You can define how precise the drawing of the corners is with the function [draw\_set\_circle\_precision()](draw_set_circle_precision.md). Please note that the rectangle being drawn may need different values (\+/\-1 on the x, y, or width or height) to be drawn with the desired dimensions due to differences across the various supported platforms.

 
 

#### Syntax:

draw\_roundrect\_colour\_ext(x1, y1, x2, y2, xrad, yrad, col1, col2, outline)

| Argument | Type | Description |
| --- | --- | --- |
| x1 | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The x coordinate of the left of the rounded rectangle. |
| y1 | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The y coordinate of the top of the rounded rectangle. |
| x2 | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The x coordinate of the right of the rounded rectangle. |
| y2 | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The y coordinate of the bottom of the rounded rectangle. |
| xrad | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The radius of the curve along the x axis from the rectangle corners. |
| yrad | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The radius of the curve along the y axis from the rectangle corners. |
| col1 | [Colour](GameMaker_Language/GML_Reference/Drawing/Colour_And_Alpha/Colour_And_Alpha.md) | The center colour. |
| col2 | [Colour](GameMaker_Language/GML_Reference/Drawing/Colour_And_Alpha/Colour_And_Alpha.md) | The outside edge colour. |
| outline | [Boolean](GameMaker_Language/GML_Overview/Data_Types.md) | Whether the rectangle is an outline (true) or filled in (false). |

 

#### Returns:

N/A

 

#### Example:

var dist \= point\_distance(x, y, mouse\_x, mouse\_y) / 10;  

 var col \= make\_colour\_hsv(clamp(dist, 0, 255\), 255, 255\);  

 draw\_roundrect\_colour\_ext(x \- 50, y \- 50, x \+ 50, y \+ 50, dist, dist, col, c\_white, 0\);

This would draw a filled\-in square with rounded corners, the radius of which is defined by the distance from the instance doing the drawing to the mouse. This value is also used to calculate the centre blend colour.
