# ds\_stack\_pop

This function will *pop* the top value off of the DS stack, removing it from the stack and returning the value to be stored in a variable. If the stack is empty then the function will return the constant undefined, otherwise it will return the real or string value contained in the stack.

 

#### Syntax:

ds\_stack\_pop(id)

| Argument | Type | Description |
| --- | --- | --- |
| id | [DS Stack](ds_stack_create.md) | The handle of the data structure to pop from. |

 

#### Returns:

[Any](../../../GML_Overview/Data_Types.md#variable) (Data type value that is stored in the stack) or [undefined](../../../GML_Overview/Data_Types.md)

 

#### Example:

if (!ds\_stack\_empty(move\_stack))  

 {  

     var xx \= ds\_stack\_pop(move\_stack);  

     var yy \= ds\_stack\_pop(move\_stack);  

     move\_towards\_point(xx, yy, 4\);  

 }

The above code checks the DS stack indexed in the variable "move\_stack" to see if it is empty, and if it is not, it then pops the top two values from the stack and use them to set a direction for movement.
