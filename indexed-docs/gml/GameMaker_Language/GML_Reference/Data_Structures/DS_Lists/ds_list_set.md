# ds\_list\_set

This function can be used to set a previously added list entry. It does the same as the [DS list accessor](../../../GML_Overview/Accessors.md).

You give the list ID (as returned when you created the list) and the position within the list to set as well as the value to set it to.

  If the entry being set is outside the bounds of the list (i.e., you set list entry 20 but the current list only contains 10 entries) then the list will be filled to the given position and each entry will be set to 0\.

 

#### Syntax:

ds\_list\_set(id, pos, val)

| Argument | Type | Description |
| --- | --- | --- |
| id | [DS List](ds_list_create.md) | The handle of the list to add to. |
| pos | [Any](../../../GML_Overview/Data_Types.md#variable) | The position within the list to set. |
| \[val2, ... max\_val] | [Any](../../../GML_Overview/Data_Types.md#variable) | The value to set in the list. |

 

#### Returns:

N/A

 

#### Example:

list \= ds\_list\_create();
   

 ds\_list\_add(list, 71, 77, 46\);
   

 ds\_list\_set(list, 2, 33\);

The above code first creates a new DS list and stores it in an instance variable list. It then adds a few values to the list add finally sets the last value (the third value at index 2\) with a call to ds\_list\_set.
