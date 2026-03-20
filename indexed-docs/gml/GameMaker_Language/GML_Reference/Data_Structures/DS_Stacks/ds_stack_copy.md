# ds\_stack\_copy

This function can be used to copy the contents of one stack (source) into another (destination). Note that this does *NOT* remove the contents from the source stack, nor does it destroy the source stack. When using this function the stack being copied to must have been previously created and if it contained any items before the copy, then these will be cleared first (meaning this information will be lost).

 

#### Syntax:

ds\_stack\_copy(destination, source)

| Argument | Type | Description |
| --- | --- | --- |
| destination | [DS Stack](ds_stack_create.md) | The handle of the new stack. |
| source | [DS Stack](ds_stack_create.md) | The original stack to copy from. |

 

#### Returns:

N/A

 

#### Example:

with (instance\_create\_layer(x, y, "Enemies", obj\_Enemy))  

 {  

     stack \= ds\_stack\_create();  

     ds\_stack\_copy(stack, other.stack);  

 }

The above function creates a new instance and then in that instance it creates a new DS stack and copies the contents of the stack in the instance running the code block, into the newly created instance stack.
