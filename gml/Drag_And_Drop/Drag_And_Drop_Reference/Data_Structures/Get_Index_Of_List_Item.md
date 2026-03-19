# title

With this action you can recover the index position of an item within the given list. You supply the variable that stores the list handle (as returned by the action [Create List](Create_List.md)) and the value you want to find the index position of within the list, as well as a target variable to store the returned index position for the item (which can be flagged as a temporary local variable to be used until the end of the script or event). Note that if the value you are looking for does not exist within the list, then there will be no list index position to return, and so the return value will be \-1\.

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| List | The handle (stored in a variable) of the list to remove from |
| Value | The value to check the list for |
| Target | The target variable to store the returned index |

 

#### Example:

The above action block code checks for a collision at the instance position and if one is found the unique ID value for the instance is stored in a temporary variable and then checked to see if it exists within the list data structure. If it does exist then the item is removed from the list and the instance destroyed.
