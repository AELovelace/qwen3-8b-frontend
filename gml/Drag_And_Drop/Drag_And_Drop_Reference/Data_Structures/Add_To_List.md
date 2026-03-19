# title

This action can be used to add a new value (of any data type) to the list, and this value will be added on at the end. You supply the variable that stores the list index (as returned by the action [Create List](Create_List.md)) and the value
 to store.

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| List | The index (stored in a variable) of the list to add to |
| Value | The value to add into the list |

 

#### Example:

The above action block code creates a global scope variable and then creates a
 new list data structure, assigning its index value to the global variable. The scope is then changed to so all the instances of the object "obj\_Enemy\_Parent" add their unique instance ID value into the list.
