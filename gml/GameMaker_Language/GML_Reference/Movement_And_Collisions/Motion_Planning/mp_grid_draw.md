# mp\_grid\_draw

This function draws the specified MP grid, marking free cells as green and forbidden cells as red.

This function is essential as a debug tool but it should be noted that it is *very* slow and only works when used in the **Draw** event of the instance, and that you can set the draw alpha to change the opacity of the grid, permitting you to draw it as an overlay and see what is actually in the room at the same time.

 

#### Syntax:

mp\_grid\_draw(id)

| Argument | Type | Description |
| --- | --- | --- |
| id | [MP Grid ID](mp_grid_create.md) | Index of the mp\_grid that is to be drawn |

 

#### Returns:

[Boolean](../../../GML_Overview/Data_Types.md)

 

#### Example:

draw\_set\_alpha(0\.3\);  

 mp\_grid\_draw(grid);  

 draw\_set\_alpha(1\);

The above code will draw the mp\_grid indexed in the variable grid as a semi\-transparent overlay (but only if the instance running the code has a depth lower than all the rest).
