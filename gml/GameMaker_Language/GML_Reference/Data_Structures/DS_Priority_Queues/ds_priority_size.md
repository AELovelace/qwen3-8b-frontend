# ds\_priority\_size

This function will return the "size" of the priority queue, ie: the number of items that have been prioritized in it.

 

#### Syntax:

ds\_priority\_size(id)

| Argument | Type | Description |
| --- | --- | --- |
| id | [DS Priority](ds_priority_create.md) | The handle of the data structure to check. |

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

if (!ds\_priority\_empty(control\_priority))  

 {  

     num \= ds\_priority\_size(control\_priority);  

 }

The above code checks a DS priority queue to see if it is empty or not, and if it is not, it gets the number of items that it contains and stores the value in a variable.
