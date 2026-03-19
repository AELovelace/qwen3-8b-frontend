# title

You can use this action to find out how many entries there are in a list. You supply the variable that holds the list index (as returned by the action [Create List](Create_List.md)) and the target variable to store the returned number of
 items in the list (which can be flagged as a temporary local variable to be used until the end of the script or event).

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| List | The index (stored in a variable) to get the item count from |
| Target | The target variable to store the returned item count |

 

#### Example:

The above action block code gets the size of the list referenced in the global
 variable and then uses a for loop to loop through it and destroy the instances with the IDs stored in the list. After the loop is finished, the list is freed from memory.
