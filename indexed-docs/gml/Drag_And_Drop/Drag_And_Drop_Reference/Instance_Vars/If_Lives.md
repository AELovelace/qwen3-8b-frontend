# title

This action is used to check the value of the instance variable lives using a specific expression. You give the type of expression to check with and the value to check the current lives against, and the "if" statement will always return either true or false depending on the expressions and values used. The available expressions are:

- **Equals to** \- The variable and the value are both exactly equal
- **Less than** \- The variable is less than the value
- **Greater than** \- The variable is greater than the value
- **Less than or Equal to** \- The variable is less than *or* equal to the value
- **Greater than or Equal to** \- The variable is greater than *or* equal to the value

If you flag the **Not** argument, then the above will be *negated expressions*, for example "equals to" becomes "*not* equals to", so you would be checking if the lives value is not equals to the given value.

 
Note that to add actions into the "if" block, they should be dropped to the side of the action, as shown in the image below:

These actions will now be run if the "if" evaluates to true, while any actions dropped elsewhere will be performed after the "if" block.

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Not | Set to check if the expression does *not* evaluate to true. |
| Expression | The type of expression to use for the check. |
| Value | The value to check the lives against. |

 

#### Example:

The above action block code will check the value of lives to see if it is less than or equal to 0 and if it is then the room will be restarted.
