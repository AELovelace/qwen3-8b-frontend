# ds\_queue\_tail

This function will only *read* the last value of the queue (that which is "at the tail"). It will not *remove* the value from the structure, meaning that it can be read again by calling this function. If the queue is empty then the function will return the constant undefined, otherwise it will return the value contained in the queue.

 

#### Syntax:

ds\_queue\_tail(id)

| Argument | Type | Description |
| --- | --- | --- |
| id | [DS Queue](ds_queue_create.md) | The handle of the data structure to read from. |

 

#### Returns:

[Any](../../../GML_Overview/Data_Types.md#variable) (Data type value stored in the queue)

 

#### Example:

num \= ds\_queue\_tail(control\_queue);

The above code will read the tail value from the queue indexed in the variable "control\_queue" and store the return value in the variable "num".
