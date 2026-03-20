# title

With this action you can set a specific cell within the grid data structure to a value. You supply the variable that holds the grid (as returned by the action [Create Grid](Create_Grid.md)) and then give the x and y position (the column and row) for the cell to set, and then finally the value for that cell. You must also set a target variable (which can be flagged as a temporary local variable) to store the returned cell value, and the value can be any valid data type. Note that the x and y position for the cell must be whole integers within the bounds of the grid.

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Grid | The index (stored in a variable) of the grid to get |
| x | The cell position along the x axis to get (the column) |
| y | The cell position along the y axis to get (the row) |
| Target | The target variable to use to store the returned value |

 

#### Example:

The above action block code gets the value in the grid stored in a global variable that corresponds to the instances position within the room. This value is then checked and if it is an instance ID value, that instance is destroyed and the grid cell set to the keyword [noone](../../../GameMaker_Language/GML_Overview/Instance Keywords/noone.md).
