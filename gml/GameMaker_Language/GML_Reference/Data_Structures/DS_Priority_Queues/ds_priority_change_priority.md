# ds\_priority\_change\_priority

This function will take a given value and change its priority within the referenced priority queue. The given value should already exist in the priority queue.

 

#### Syntax:

ds\_priority\_change\_priority(id, val, priority)

| Argument | Type | Description |
| --- | --- | --- |
| id | [DS Priority](ds_priority_create.md) | The handle of the priority queue to change. |
| val | [Any](../../../GML_Overview/Data_Types.md#variable) | The value to change the priority of. |
| priority | [Real](../../../GML_Overview/Data_Types.md) | The new priority of the value. |

 

#### Returns:

N/A

 

#### Example:

if (global.Game\_Time \< 1000\)  

 {  

     ds\_priority\_change(ai\_priority, AI\_Search, 1\);  

 }

The above code checks a global variable and if it is below a certain value it will then change the priority of the script function index held in the priority queue.
