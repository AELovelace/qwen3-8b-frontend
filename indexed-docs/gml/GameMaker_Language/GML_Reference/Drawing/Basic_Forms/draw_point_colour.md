# draw\_point\_colour

With this function you can draw a single pixel anywhere on the screen with a colour that you define. The colour settings will override the base colour set with the function [draw\_set\_colour()](../Colour_And_Alpha/draw_set_colour.md).

 
 

#### Syntax:

draw\_point\_colour(x, y, col1\)

| Argument | Type | Description |
| --- | --- | --- |
| x | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The x coordinate of the point. |
| y | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The y coordinate of the point. |
| col1 | [Colour](GameMaker_Language/GML_Reference/Drawing/Colour_And_Alpha/Colour_And_Alpha.md) | The colour of the point. |

 

#### Returns:

N/A

 

#### Example:

draw\_point\_colour(50, 50, c\_red);

This would draw a red pixel at (50,50\).
