# ds\_stack\_destroy

This function will remove the given stack data structure from memory, freeing up the resources it was using and removing all values that it contained. This function should always be used when you are finished using the DS stack to prevent memory leaks that can slow down and crash your game.

 
 

#### Syntax:

ds\_stack\_destroy(id)

| Argument | Type | Description |
| --- | --- | --- |
| id | [DS Stack](ds_stack_create.md) | The stack data structure to remove |

 

#### Returns:

N/A

 

#### Example:

if (lives \=\= 0\)  

 {  

     ds\_stack\_destroy(AI\_stack);  

     AI\_stack \= \-1;  

     room\_goto(rm\_Menu);  

 }

The above code will check the value of the built\-in global variable [lives](../../../GML_Overview/Variables/Builtin_Global_Variables/lives.md) and if it is 0, it destroys the DS stack referenced in the variable AI\_stack and then changes rooms.
