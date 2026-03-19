# yprevious

This built\-in variable returns the *previous* y position for the instance. This variable will be set to the current x position when an instance is created and just before the start of the **Begin Step event** but it can also be set through code at any time, meaning you can give it your own custom value should that be necessary.

 

#### Syntax:

yprevious

 

#### Returns:

[Real](../../../../GML_Overview/Data_Types.md) (single precision floating point value)

 

#### Example:

if (x !\= xprevious \|\| y !\= yprevious)  

 {  

     moved \= true;  

 }

The above code checks to see if there is any difference between the xprevious and yprevious values and the current x and y values. If there is, it sets a variable to true.
