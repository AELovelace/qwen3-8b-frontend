# mp\_grid\_clear\_rectangle

With this function you can define an area *in room coordinates* which will then clear the corresponding cells in the specified MP grid. Even if a cell partially falls within the defined rectangular region it will be cleared.

 

#### Syntax:

mp\_grid\_clear\_rectangle(id, x1, y1, x2, y2\)

| Argument | Type | Description |
| --- | --- | --- |
| id | [MP Grid ID](mp_grid_create.md) | Index of the mp\_grid that is to be used |
| x1 | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate of the left side of the rectangle to check |
| y1 | [Real](../../../GML_Overview/Data_Types.md) | The y coordinate of the top side of the rectangle to check |
| x2 | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate of the right side of the rectangle to check |
| y2 | [Real](../../../GML_Overview/Data_Types.md) | The x coordinate of the bottom side of the rectangle to check |

 

#### Returns:

[Boolean](../../../GML_Overview/Data_Types.md)

 

#### Example:

mp\_grid\_clear\_rectangle(grid, 0, 0, 100, 200\);

The above code will mark as free all cells of the mp\_grid indexed in the variable grid that fall within the area (0, 0\) to (100, 200\).
