# ds\_list\_replace

This function will replace the value at the given position for another one.

  Attempting to replace an item at a position out of bounds results in an error, e.g. ds\_list\_replace :: Trying to access an out\-of\-bounds index \[\| 4].

 

#### Syntax:

ds\_list\_replace(id, pos, val)

| Argument | Type | Description |
| --- | --- | --- |
| id | [DS List ID](GameMaker_Language/GML_Reference/Data_Structures/DS_Lists/ds_list_create.md) | The handle of the list to change. |
| pos | [Real](GameMaker_Language/GML_Overview/Data_Types.md) | The position to replace the value, where 0 corresponds to the very beginning of the list and the final position is ds\_list\_size(id)\-1. |
| val | [Any](GameMaker_Language/GML_Overview/Data_Types.md#variable) | The new value to replace the given value with. |

 

#### Returns:

N/A

 

#### Example:

ds\_list\_replace(n\_list, 3, name);

The above code will replace the value stored at position 3 in the list for that stored in the variable "name".
