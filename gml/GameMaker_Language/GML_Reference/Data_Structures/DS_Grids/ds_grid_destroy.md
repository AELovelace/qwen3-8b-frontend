# ds\_grid\_destroy

This function will remove the given grid data structure from memory, freeing up the resources it was using and removing all values that it contained. This function should always be used when you are finished using the DS grid to prevent memory leaks that can slow down and crash your game.

 
 

#### Syntax:

ds\_grid\_destroy(index)

| Argument | Type | Description |
| --- | --- | --- |
| index | [DS Grid](ds_grid_create.md) | The grid to destroy |

 

#### Returns:

N/A

 

#### Example:

if (lives \=\= 0\)  

 {  

     ds\_grid\_destroy(Wall\_Grid);  

     Wall\_Grid \= \-1;  

     room\_goto(rm\_Menu);  

 }

The above code will check the value of the built\-in global variable [lives](../../../GML_Overview/Variables/Builtin_Global_Variables/lives.md) and if it is 0, it destroys the DS grid referenced in the variable Wall\_Grid and then changes rooms.
