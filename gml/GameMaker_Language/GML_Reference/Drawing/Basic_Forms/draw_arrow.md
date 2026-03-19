# draw\_arrow

This function will draw an arrow from point (x1,y1\) to point (x2,y2\). The stem of the arrow is drawn along these points with the actual arrow head being drawn at the end, where the size of the arrowhead is defined by the argument "size" and is calculated as being part of the stem so that the end point is always aligned with the position defined by x2,y2\. The width of the arrow head is calculated automatically in proportion to the length.

 
 

#### Syntax:

draw\_arrow(x1, y1, x2, y2, size)

 

| Argument | Type | Description |
| --- | --- | --- |
| x1 | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The x coordinate of the start of the line. |
| y1 | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The y coordinate of the start of the line. |
| x2 | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The x coordinate of the end of the line (where the arrowhead ends). |
| y2 | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The y coordinate of the end of the line (where the arrowhead ends). |
| size | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The length of the arrow in pixels. |

 

#### Returns:

N/A

 

#### Example:

draw\_arrow(x, y, mouse\_x, mouse\_y, 10\);

The above code will draw an arrow from the position of the instance to the position of the mouse, with the arrow head being 10 pixels long.
