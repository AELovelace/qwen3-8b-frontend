# Get Global Variable

This action is used to retrieve the value of a global variable and assign it to another instance or temporary (local) variable. The variable you assign the global value to can be one that was previously created, or you can check the "Temp" checkbox and give a new variable name to have the action create a new temporary (local) variable specifically to hold the returned value.

Note that you can add additional variables in the same action by clicking the plus icon  beside the action, and giving another global variable name and temporary local variable name. For more advanced information on variables please see the section on [Variables And Variable Scope](../../../GameMaker_Language/GML_Overview/Variables_And_Variable_Scope.md).

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Name | The name of the global variable to get the value of. |
| Target | The target variable to hold the returned value \- it should have been created previously if "Temp" is not checked (see below). |
| Temp | Create a temporary (local) variable to hold the returned value (off by default) |

 

#### Example:

The above action block code retrieves two global variable values and assigns them to temporary (local) variables which are then used in an "if" comparison. If the result is true, three global variables are set to new values.
