# math\_get\_epsilon

This function returns the current epsilon value.

The default epsilon value is 0\.00001.

For more information on epsilon, please see the function [math\_set\_epsilon](math_set_epsilon.md).

 

#### Syntax:

math\_get\_epsilon()

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

var e \= math\_get\_epsilon();  

 if (e !\= 0\.000001\)  

 {  

     math\_set\_epsilon(0\.000001\);  

 }

This will retrieve the current epsilon value and store it in a local variable, which is then checked and a new epsilon set if required.
