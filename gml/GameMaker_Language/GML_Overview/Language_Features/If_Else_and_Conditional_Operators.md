# if / else and Conditional Operators

A fundamental feature of most programming languages is the ability to ask a simple question that gives a boolean true or false answer, and in GML this is achieved using the if keyword. A simple if condition takes an [expression](#) and will perform one or more [statement](#)s if the expression resolves as true, with the following basic form:

if (\)  

 {  

     \;  

     \;  

     ...  

 }

Here you are saying that if an expression resolves to true then do something. Note that the "then" part of the condition is *implicit*, but there is a then keyword that can be used (although it's almost always omitted), so you can also create conditionals like this:

if (\) then  

 {  

     \;  

     \;  

     ...  

 }

Apart from if and then, you can also use the else keyword to do something else if the expression being checked evaluates as false. This "if... then... else..." form looks like this:

if (\)  

 {  

     \;  

 }  

 else  

 {  

     \;  

 }

In this case the expression will be evaluated, and if it evaluates to false, the statement after else is executed, otherwise the initial statement is executed (it's true).

  In the GameMaker Language any numeric value that is less than or equal to 0\.5 will evaluate as false, while any value that is greater than 0\.5 will evaluate as true.

## Grouping Expressions \& Statements

It is a good habit to always put parentheses () around the expressions and curly brackets {} around the statements in the if (otherwise only the first statement will be executed), and take a new line in the block for each statement, for example:

// This will work  

 if \ \;  

  

 // Example:  

 if test \=\= true variable \= false else variable \= true;
 

// This is better  

 if (\)  

 {  

     \;  

 }  

 else  

 {  

     \;  

 }  

  

 // Example  

 if (test \=\= true)  

 {  

     variable \= false;  

 }  

 else  

 {  

     variable \= true;  

 }
 

Note that while this is slightly more verbose, it means that there is no ambiguity in the code and that it will compile correctly on all platforms at all times. However, the initial example may not, as explained on the section in the [Expressions And Operators](../Expressions_And_Operators.md) page.

  When comparing two values to see if they are equal, you should use the \=\= operator, and only use the \= one for assignment. Currently GameMaker will treat them as interchangeable, but this may change in the future and your code is cleaner and more obvious when using the correct operators for comparisons and assignments.

To give a proper example of using if, consider the following code which will move an instance towards the position x\=200 in the room when placed in the Step Event:

if (x \< 200\)  

 {  

     x \+\= 4;  

 }  

 else  

 {  

     x \= 200;  

 }

## Compound Checks

Note that you can also do *compound* checks in an if, i.e.: check various values or expressions in the same statement. These checks can use the various [Combining Operators](../Expressions_And_Operators.md) (\&\& (and), \|\| (or), and ^^ (xor)). When you do this, GameMaker will evaluate each of them one at a time, and depending on how they evaluate, the rest may be skipped. For example:

if (keyboard\_check\_pressed(vk\_enter)) \&\& (instance\_exists(obj\_player))  

 {  

     go \= false;  

     alarm\[0] \= game\_get\_speed(gamespeed\_fps);  

 }

Here we are checking using the \&\& (and) operator, so it's checking if *both* of the conditions in the if evaluate to true, and if the first one is false then the second one won't even be checked.

This is called "short\-circuiting" the code, so when combining expressions to check, you should ensure that the "cheapest" one for performance is always the first to avoid evaluating the more expensive ones if the first evaluates to false.

In a similar vein, if a condition can be evaluated as true or false at compile time, then the entire condition will be removed from the code, for example, say you have a [macro](../Variables/Constants.md) DEBUG\_ON for debugging and it can be either true or false \- when it is set to false then the following code block will be stripped from the game when it is compiled:

if (DEBUG\_ON \=\= true)  

 {  

     show\_debug\_message("Instances \= " \+ string(instance\_count));  

 }

## Ternary Operators

You can also perform **conditional operations** (also know as **ternary** operations), which is essentially a "shortcut" way of performing a basic if.
