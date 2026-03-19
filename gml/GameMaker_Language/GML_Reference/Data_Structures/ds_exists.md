# ds\_exists

This function checks if a data structure of the given type with the given index exists.

You supply the DS reference (as held in a variable) and the DS type, which can be any of the constants listed below, and the function will return true if the data structure exists and false otherwise.

| [DS Type Constant](ds_exists.md) | |
| --- | --- |
| Constant | Description |
| ds\_type\_map | A [map](DS_Maps/DS_Maps.md) data structure |
| ds\_type\_list | A [list](DS_Lists/DS_Lists.md) data structure |
| ds\_type\_stack | A [stack](DS_Stacks/DS_Stacks.md) data structure |
| ds\_type\_grid | A [grid](DS_Grids/DS_Grids.md) data structure |
| ds\_type\_queue | A [queue](DS_Queues/DS_Queues.md) data structure |
| ds\_type\_priority | A [priority](DS_Priority_Queues/DS_Priority_Queues.md) data structure |

  You cannot use this function to check the type of a data structure, as the same index number may be used by multiple data structures of differing types.

 

#### Syntax:

ds\_exists(ind, type)

| Argument | Type | Description |
| --- | --- | --- |
| ind | [Any DS Reference](Data_Structures.md) | The variable index to check for the data structure |
| type | [DS Type Constant](ds_exists.md) | The type of data structure to check for (see the list of constants above) |

 

#### Returns:

[Boolean](../../GML_Overview/Data_Types.md)

 

#### Example:

if (!ds\_exists(ai\_grid, ds\_type\_grid))  

 {  

     ai\_grid \= ds\_grid\_create(room\_width / 32, room\_height / 32\);  

 }

The above code checks the (previously initialised) variable ai\_grid to see if it indexes a DS grid type data structure. If it doesn't, it creates one and stores its handle in the variable.
