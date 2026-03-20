# draw\_line\_width

With this function you can draw a line of a specified width between any two points in the game room. Please note that the line being drawn may need different values (\+/\-1 on the x, y) to be drawn with the desired dimensions due to differences across the various supported platforms.

 
 

#### Syntax:

draw\_line\_width(x1, y1, x2, y2, w)

| Argument | Type | Description |
| --- | --- | --- |
| x1 | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The x coordinate of the start of the line. |
| y1 | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The y coordinate of the start of the line. |
| x2 | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The x coordinate of the end of the line. |
| y2 | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The y coordinate of the end of the line. |
| w | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The width of the line in pixels. |

 

#### Returns:

N/A

 

#### Example:

draw\_set\_colour(c\_red);  

 draw\_line\_width(100, 100, 200, 200, 6\);

This will draw a red diagonal line, 6 pixels wide, from point (100,100\) to point (200,200\).
