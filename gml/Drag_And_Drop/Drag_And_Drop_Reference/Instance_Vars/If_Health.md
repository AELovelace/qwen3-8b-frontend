# title

This action is used to check the value of the instance variable health using a specific expression. You give the type of expression to check with and the value to check the current health against, and the "if" statement will always return either true or false depending on the expressions and values used. The available expressions are:

- **Equals to** \- The variable and the value are both exactly equal
- **Less than** \- The variable is less than the value
- **Greater than** \- The variable is greater than the value
- **Less than or Equal to** \- The variable is less than *or* equal to the value
- **Greater than or Equal to** \- The variable is greater than *or* equal to the value

If you flag the **Not** argument, then the above will be *negated expressions*, for example "equals to" becomes "*not* equals to", so you would be checking if the health value is not equals to the given value.

  Due to [floating point precision issues](https://floating-point-gui.de/formats/fp/), checking to see if two values are exactly equal may return false, since one may be exactly 1, while the other may be 1\.00000000000001\. This can be avoided by using the [Decimal to Integer](../Data_Types/Decimal_To_Integer.md) action before checking or using the "greater than" or "less than" expressions.

Note that to add actions into the "if" block, they should be dropped to the side of the action, as shown in the image below:

These actions will now be run if the "if" evaluates to true, while any actions dropped elsewhere will be performed after the "if" block.

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Not | Set to check if the expression does *not* evaluate to true. |
| Expression | The type of expression to use for the check. |
| Value | The value to check the health against. |

 

#### Example:

The above action block code will add 25 onto the health variable and then check to see if the variable is now greater than 100, and if it is it will be set to 100\.
