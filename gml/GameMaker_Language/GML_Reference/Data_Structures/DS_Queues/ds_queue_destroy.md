# ds\_queue\_destroy

This function will remove the given queue data structure from memory, freeing up the resources it was using and removing all values that it contained. This function should always be used when you are finished using the DS queue to prevent memory leaks that can slow down and crash your game.

 
 

#### Syntax:

ds\_queue\_destroy(id)

| Argument | Type | Description |
| --- | --- | --- |
| id | [DS Queue](ds_queue_create.md) | The queue data structure to remove |

 

#### Returns:

N/A

 

#### Example:

if (lives \=\= 0\)  

 {  

     ds\_queue\_destroy(AI\_queue);  

     AI\_queue \= \-1;  

     room\_goto(rm\_Menu);  

 }

The above code will check the value of the built\-in global variable [lives](../../../GML_Overview/Variables/Builtin_Global_Variables/lives.md) and if it is 0, it destroys the DS queue referenced in the variable AI\_queue and then changes rooms.
