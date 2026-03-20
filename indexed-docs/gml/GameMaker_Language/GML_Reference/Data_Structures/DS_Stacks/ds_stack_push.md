# ds\_stack\_push

This function will *push* (add) a value, which can be of any data type, onto the top of the stack. The function can take any number of additional arguments, permitting you to push multiple values consecutively to the stack in a single call.

 

#### Syntax:

ds\_stack\_push(id, val \[, val2, ...])

| Argument | Type | Description |
| --- | --- | --- |
| id | [DS Stack](ds_stack_create.md) | The handle of the data structure to push onto. |
| val | [Any](../../../GML_Overview/Data_Types.md#variable) | The value to push onto the stack. |
| \[val2, ...] | [Any](../../../GML_Overview/Data_Types.md#variable) | Optional values to be added to the stack, each one a new argument. |

 

#### Returns:

N/A

 

#### Example:

move\_stack \= ds\_stack\_create();
   

 ds\_stack\_push(move\_stack, x, y, x, y \+ 200, x \+ 200, y \+ 200, x \+ 200, y);

The above code creates a new DS stack and stores its index in the variable "move\_stack". It then pushes a number of values onto the stack for future use.
