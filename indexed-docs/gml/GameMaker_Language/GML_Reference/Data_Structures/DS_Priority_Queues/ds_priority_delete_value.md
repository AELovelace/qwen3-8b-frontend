# ds\_priority\_delete\_value

This function will simply delete the given value, along with its priority, from the indexed priority queue.

 

#### Syntax:

ds\_priority\_delete\_value(id,val)

| Argument | Type | Description |
| --- | --- | --- |
| id | [DS Priority](ds_priority_create.md) | The handle of the priority queue to use. |
| val | [Any](../../../GML_Overview/Data_Types.md#variable) | The value to delete from the priority queue. |

 

#### Returns:

N/A

 

#### Example:

if (ai\_move \=\= false)  

 {  

     ds\_priority\_delete\_value(ai\_priority, AI\_Move);  

 }

The above code checks an instance variable and if it returns false it will remove the indexed script function from the priority queue.
