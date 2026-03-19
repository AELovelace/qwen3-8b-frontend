# ds\_stack\_clear

With this function you can clear all data from the given stack data structure. This does *NOT* destroy the data structure (for that you should use [ds\_stack\_destroy()](ds_stack_destroy.md)) it only wipes all data from it and returns an empty stack.

 

#### Syntax:

ds\_stack\_clear(id)

| Argument | Type | Description |
| --- | --- | --- |
| id | [DS Stack](ds_stack_create.md) | The handle of the data structure to clear. |

 

#### Returns:

N/A

 

#### Example:

if (ai\_count \= 15 \&\& !ds\_stack\_empty(AI\_stack))  

 {  

     ds\_stack\_clear(AI\_stack);  

     alarm\[0] \= game\_get\_speed(gamespeed\_fps);  

     ai\_count \= 0;  

 }

The above code checks a variable to see if it has reached a specific value and if it has it clears the DS stack indexed in the variable "AI\_stack", sets an alarm, and resets the variable to 0\.
