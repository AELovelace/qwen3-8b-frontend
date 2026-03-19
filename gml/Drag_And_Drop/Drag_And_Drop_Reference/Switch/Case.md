# Case

This action will create a new Case within a [Switch](Switch.md). You give the value for the case and it will be compared with the input value for the Switch, and if they match the actions added under the Case will be performed.
 Actions that are added to a Case to be performed *only* in that Case should be dropped to the side of the action, much as you would add an action to an "if":

Note that a Case value *must be a constant*, which can be any data type (real, string, etc...),
 as long as it evaluates to a single value on compile \- so you can't use expressions that depend on variables. Also note that Case cannot be used outside of a Switch and trying to do so will give you an error.

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Constant | The constant value to be evaluated against the Switch input value |

 

#### Example:

The above action block code gets the value stored in a variable and then compares it to
 the different possible cases. If any one of the cases is the same as the value, then the action under that case will be performed, otherwise the next case will be evaluated. After the switch has run, an alarm is set to 30\.
