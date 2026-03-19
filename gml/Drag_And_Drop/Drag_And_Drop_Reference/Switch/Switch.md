# Switch

This action will create a new Switch statement to which you can then add further cases for evaluation. You give the value that is to be used for comparing to the cases in the Switch and then add the different [Case](Case.md) actions, much
 as you would add an action to an "if", ie: dropping it to the side of the action rather than under it:

Note that you cannot add any other type of action into a switch without first having added at least one
 Case to contain it.

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Value | The value to be used by the switch for evaluation |

 

#### Example:

The above action block code gets the value stored in a variable and then compares it to the different possible
 cases. If any one of the cases is the same as the value, then the action under that case will be performed, otherwise the next case will be evaluated. After the switch has run, an alarm is set to 30\.
