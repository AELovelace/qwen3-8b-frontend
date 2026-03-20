# title

With this action you can push a value onto a stack data structure. You supply the variable that holds the stack index (as returned by the action [Create Stack](Create_Stack.md)) and then give the value to push onto the top. With stack data
 structures, values are always added onto the "top" of the stack, and never at the end or in the middle (if you require this functionality, then use a list data structure).

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Stack | The index (stored in a variable) of the stack to use |
| Value | The value to push onto the stack |

 

#### Example:

The above action block code creates an instance variable and a new stack data structure.
 The index of the stack is stored in the new variable, and then a loop is performed which creates 10 instances and pushes their unique ID values onto the stack.
