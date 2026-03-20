# ds\_priority\_find\_min

With this function you can find the value stored in the priority queue with the lowest priority, and if more than one value has the same priority then any one of them could be returned in any order. However, unlike [ds\_priority\_delete\_min()](ds_priority_delete_min.md), this function will not remove the value from the queue.

 
 

#### Syntax:

ds\_priority\_find\_min(id)

| Argument | Type | Description |
| --- | --- | --- |
| id | [DS Priority](ds_priority_create.md) | The handle of the priority queue to use. |

 

#### Returns:

[Any](../../../GML_Overview/Data_Types.md#variable) (Data type stored in the priority)

 

#### Example:

if (ai\_move)  

 {  

     script\_execute(ds\_priority\_find\_min(ai\_priority));  

 }

The above code checks an instance variable and if it returns true it will execute a script function indexed in the priority queue with the lowest priority value.
