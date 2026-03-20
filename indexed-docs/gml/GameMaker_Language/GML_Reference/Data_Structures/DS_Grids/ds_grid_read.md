# ds\_grid\_read

This function can be used to convert a string which has been created previously by the function [ds\_grid\_write()](ds_grid_write.md) back into a DS grid. The DS grid must have been created previously (see the example below).

 
 

#### Syntax:

ds\_grid\_read(index, string \[, legacy])

| Argument | Type | Description |
| --- | --- | --- |
| index | [DS Grid](ds_grid_create.md) | The handle of the grid to read. |
| string | [String](../../../GML_Overview/Data_Types.md) | The string to read into the DS grid. |
| legacy | [Boolean](../../../GML_Overview/Data_Types.md) | Can be either true or false or omitted completely. |

 

#### Returns:

N/A

 

#### Example:

grid \= ds\_grid\_create(room\_width div 32, room\_height div 32\);  

 ini\_open("Save.ini");  

 ds\_grid\_read(grid, ini\_read\_string("Save", "0", ""));  

 ini\_close();

The above code creates a DS grid based on the size of the room (each 32x32 square of pixels represents one grid cell) and then reads a previously saved set of grid data from an ini file into the new DS grid.
