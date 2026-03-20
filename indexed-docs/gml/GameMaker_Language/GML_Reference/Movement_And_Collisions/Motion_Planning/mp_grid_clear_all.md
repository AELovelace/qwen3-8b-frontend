# mp\_grid\_clear\_all

This function clears an MP grid of all "forbidden" cells.

 

#### Syntax:

mp\_grid\_clear\_all(id)

| Argument | Type | Description |
| --- | --- | --- |
| id | [MP Grid ID](mp_grid_create.md) | Index of the mp\_grid to clear |

 

#### Returns:

[Boolean](../../../GML_Overview/Data_Types.md)

 

#### Example:

if (!instance\_exists(obj\_player))  

 {  

     mp\_grid\_clear\_all(grid);  

 }

The above code will clear the mp\_grid indexed in the variable grid, marking all the cells as free, if an instance of the object obj\_player no longer exists in the room.
