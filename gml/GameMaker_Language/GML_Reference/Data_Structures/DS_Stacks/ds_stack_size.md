# ds\_stack\_size

This function will return the "size" of the stack, ie: the number of items that have been pushed onto it.

 

#### Syntax:

ds\_stack\_size(id)

| Argument | Type | Description |
| --- | --- | --- |
| id | [DS Stack](ds_stack_create.md) | The handle of the data structure to check. |

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

if (!ds\_stack\_empty(control\_stack))  

 {  

     num \= ds\_stack\_size(control\_stack);  

 }

The above code checks a DS stack to see if it is empty or not, and if it is not, it gets the number of items that it contains and stores the value in a variable.
