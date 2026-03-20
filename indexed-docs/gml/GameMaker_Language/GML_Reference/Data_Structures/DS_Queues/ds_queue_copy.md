# ds\_queue\_copy

This function can be used to copy the contents of one queue (source) into another (destination). Note that this does *NOT* remove the contents from the source queue, nor does it destroy the source queue. When using this function the queue being copied to must have been previously created and if it contained any items before the copy, then these will be cleared first (meaning this information will be lost).

 

#### Syntax:

ds\_queue\_copy(destination, source)

| Argument | Type | Description |
| --- | --- | --- |
| destination | [DS Queue](ds_queue_create.md) | The handle of the new queue. |
| source | [DS Queue](ds_queue_create.md) | The original queue to copy from. |

 

#### Returns:

N/A

 

#### Example:

with (instance\_create\_layer(x, y, "Enemies", obj\_Enemy))  

 {  

     queue \= ds\_queue\_create();  

     ds\_queue\_copy(queue, other.queue);  

 }

The above function creates a new instance and then in that instance it creates a new DS queue and copies the contents of the queue in the instance running the code block, into the newly created instance queue.
