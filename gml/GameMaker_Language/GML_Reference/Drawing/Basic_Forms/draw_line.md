# draw\_line

With this function you can draw a 1 pixel wide line between any two points in the game room. Please note that the line being drawn may need different values (\+/\-1 on the x, y) to be drawn with the desired dimensions due to differences across the various supported platforms.

 
 

#### Syntax:

draw\_line(x1, y1, x2, y2\)

| Argument | Type | Description |
| --- | --- | --- |
| x1 | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The x coordinate of the start of the line. |
| y1 | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The y coordinate of the start of the line. |
| x2 | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The x coordinate of the end of the line. |
| y2 | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The y coordinate of the end of the line. |

 

#### Returns:

N/A

 

#### Example:

draw\_set\_colour(c\_lime);  

 draw\_line(50,50,150,50\);

This will draw a light green horizontal line from point (50,50\) to point (150,50\).
