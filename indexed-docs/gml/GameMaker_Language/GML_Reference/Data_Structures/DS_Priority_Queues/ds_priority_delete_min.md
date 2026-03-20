# ds\_priority\_delete\_min

This function will return the value that has the lowest priority in the queue and then remove the value (and priority) from the data structure. If more than one value has the same priority, then any one of them could be returned in any order, but all other values with the same priority will still be in the queue.

  If the priority queue is empty, this function will return 0\.

 

#### Syntax:

ds\_priority\_delete\_min(id)

| Argument | Type | Description |
| --- | --- | --- |
| id | [DS Priority](ds_priority_create.md) | The handle of the priority queue to use. |

 

#### Returns:

[Any](../../../GML_Overview/Data_Types.md#variable) (Data type stored in the priority)

 

#### Example:

if (ai\_move)  

 {  

     script\_execute(ds\_priority\_delete\_min(ai\_priority));  

 }

The above code checks an instance variable and if it returns true it will execute a script function indexed in the priority queue with the lowest priority value and then remove that script from the queue.
