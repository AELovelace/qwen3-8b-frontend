# title

With this action you can recover the index position of an item within the given list. You supply the variable that stores the list index (as returned by the action [Create List](Create_List.md)) and the index position within the list to get the item value from, as well as a target variable to store the returned item value (which can be flagged as a temporary local variable to be used until the end of the script or event).

  If you give a position that is outside of the given list size (ie: position 11 in a 10 value list) then the action will return undefined. You can check for this using the [If Undefined](../Common/If_Undefined.md) action.

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| List | The index (stored in a variable) of the list to remove from |
| Index | The index position within the list to get the item from |
| Target | The target variable to store the returned value |

 

#### Example:

The above action block code gets the size of the list referenced in the global variable and then uses a for loop to loop through it and destroy the instances with the IDs stored in the list. After the loop is finished, the list is freed from memory.
