# ds\_queue\_dequeue

This function will *dequeue* the head value off of the DS queue, removing it from the queue and returning the value to be stored in a variable. If the queue is empty then the function will return the constant undefined, otherwise it will return the value contained in the queue.

 

#### Syntax:

ds\_queue\_dequeue(id)

| Argument | Type | Description |
| --- | --- | --- |
| id | [DS Queue](ds_queue_create.md) | The handle of the queue to dequeue from. |

 

 

#### Returns:

[Any](../../../GML_Overview/Data_Types.md#variable) (Data type value stored in the queue) or [undefined](../../../GML_Overview/Data_Types.md)

 

#### Example:

if (!ds\_queue\_empty(move\_queue))  

 {  

     var xx \= ds\_queue\_dequeue(move\_queue);  

     var yy \= ds\_queue\_dequeue(move\_queue);  

     move\_towards\_point(xx, yy, 4\);  

 }

The above code checks the DS queue indexed in the variable "move\_queue" to see if it is empty, and if it is not, it then dequeues the two values from the head of the queue and use them to set a direction for movement.
