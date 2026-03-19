# title

With this action you can pop a value off the top of a stack data structure. You supply the variable that holds the stack index (as returned by the action [Create Stack](Create_Stack.md)) and then give the target variable that should hold
 the returned variable (which can be flagged as a temporary local variable).

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Stack | The index (stored in a variable) of the stack to use |
| Target | The target variable to hold the returned value |

 

#### Example:

The above action block code checks to see if the given stack is empty, and if it is not, it pops
 the top value off and stores it in a temporary variable. This is then used to set an alarm, while if the stack is empty, 10 random values are pushed onto the stack.
