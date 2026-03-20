# Else

The "Else" action is *only ever used in conjunction with [If Variable](If_Variable.md)*(or any other "if" action), and is a way of defining a set of actions that should be performed if the "if" evaluation returns false. For example, you could have an "if" action that checks if the players health variable is less than or equal to 0, and if that evaluates to true you destroy the instance. However if you want to perform a different set of code actions if the player health is *not* less than 0 then you can add an "else" in and then specify the actions to be performed while the if evaluates to false.

Note that to add actions into the "else" block, they should be dropped to the side of the action, as shown in the image below:

Any actions dropped elsewhere will be performed after the "else" block and its contents have been run.

 

#### Action Syntax:

#### Example:

The above action block code checks a DS list to see if the initial value is "undefined" or not. If it is then the DS List is destroyed, otherwise the value is assigned to a global variable.
