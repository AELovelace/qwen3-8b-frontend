# mp\_grid\_destroy

This function destroys the given MP grid and frees up the memory used by it. It is *essential* that you call this whenever the MP grid is finished with or you could potentially get a memory leak, meaning that your game will slow down over time and eventually crash.

  Using mp\_grid\_\* functions on a grid after it has been destroyed will result in an error.

 

#### Syntax:

mp\_grid\_destroy(id)

| Argument | Type | Description |
| --- | --- | --- |
| id | [MP Grid ID](mp_grid_create.md) | The MP grid to destroy |

 

#### Returns:

N/A

 

#### Example:

if (timer \=\= 0\)  

 {  

     mp\_grid\_destroy(grid);  

     room\_goto(rm\_menu);  

 }

The above code will destroy the mp\_grid indexed in the variable grid if the variable timer is equal to 0, and then goto another room.
