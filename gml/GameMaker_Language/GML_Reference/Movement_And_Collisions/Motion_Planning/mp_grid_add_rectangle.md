# mp\_grid\_add\_rectangle

This function takes a rectangle in room coordinates and marks all MP grid cells that "touch" that rectangle as forbidden, meaning that the pathfinding functions cannot cross them.

The image below illustrates how this works:

As you can see, the rectangle defined by (50, 90\) to (200, 180\) marks all the equivalent MP grid cells that it touches as being forbidden.

 

#### Syntax:

mp\_grid\_add\_rectangle(id, x1, y1, x2, y2\)

| Argument | Type | Description |
| --- | --- | --- |
| id | [MP Grid ID](mp_grid_create.md) | Index of the mp\_grid that is to be used |
| x1 | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate of the left side of the rectangle to check |
| y1 | [Real](../../../GML_Overview/Data_Types.md) | The y coordinate of the top side of the rectangle to check |
| x2 | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate of the right side of the rectangle to check |
| y2 | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate of the bottom side of the rectangle to check |

 

#### Returns:

N/A

 

#### Example:

mp\_grid\_add\_rectangle(grid, 0, 0, 100, 200\);

The above code will mark as forbidden all cells of the mp\_grid indexed in the variable grid that fall within the area (0, 0\) to (100, 200\).
