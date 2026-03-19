# ds\_queue\_empty

With this function you can check the given DS queue to see if it is empty (returns true) or not (returns false).

 

#### Syntax:

ds\_queue\_empty(id)

| Argument | Type | Description |
| --- | --- | --- |
| id | [DS Queue](ds_queue_create.md) | The handle of the data structure to check. |

 

#### Returns:

[Boolean](../../../GML_Overview/Data_Types.md)

 

#### Example:

if (count \=\= 15\) \&\& (!ds\_queue\_empty(command\_queue))  

 {  

     ds\_queue\_clear(command\_queue);  

     alarm\[0] \= game\_get\_speed(gamespeed\_fps);  

     ai\_count \= 0;  

 }

The above code checks a variable to see if it has reached a specific value and if it has it clears the DS queue indexed in the variable "command\_queue", sets an alarm, and resets the variable to 0\.
