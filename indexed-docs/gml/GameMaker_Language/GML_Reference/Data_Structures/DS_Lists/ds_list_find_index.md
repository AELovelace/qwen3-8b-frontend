# ds\_list\_find\_index

With this function you can check the given list for a value and the position within the list for that value will be returned.

Note that if there are multiple entries in the list with the same value, the position of any one of them may be returned, and if the value doesn't exist, \-1 will be returned.

 

#### Syntax:

ds\_list\_find\_index(id, val)

| Argument | Type | Description |
| --- | --- | --- |
| id | [DS List](ds_list_create.md) | The handle of the list to use. |
| val | [Any](../../../GML_Overview/Data_Types.md#variable) | The value to find. |

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

pos \= ds\_list\_find\_index(list, "Player1");

The above code checks the list indexed in the variable "list" for the value "Player1" and stores the returned position in the variable "pos".
