# If Undefined

This action is used to check if a variable or expression returns a value of "undefined", and if it is then this action will return true and if it isn't it will return false. "Undefined" can be returned for a number of reasons, and an undefined value can cause a crash or serious error in your project, so you can use this to check for that and catch it before it happens. If you flag the "Not" argument, then you are checking to see if a value is *not* "undefined".

Note that to add actions into the "if" block, they should be dropped to the side of the action, as shown in the image below:

These actions will now be run if the "if" evaluates to true, while any actions dropped elsewhere will be performed after the "if" block. Note that you can "stack" undefined checks in the same action by clicking the plus icon  beside the action, and giving another variable to check. This will check if *all* the variables given are undefined in one check and only perform the added action code if they are.

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Variable | The name of the variable to check. |
| Not | Set to check if undefined does *not* evaluate to true. |

 

#### Example:

The above action block code checks a DS list to see if the initial value is "undefined" or not, and if it is then the list is destroyed.
