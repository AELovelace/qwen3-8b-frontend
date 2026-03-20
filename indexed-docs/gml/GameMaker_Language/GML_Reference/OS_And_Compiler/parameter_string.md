# parameter\_string

This function returns the value of the command\-line parameter at the given position.

Command\-line parameters are those extra commands that you can pass to an exe to change how the program is run.

You can find the number of parameters for the current game using the function [parameter\_count](parameter_count.md), where the first parameter has index 1 and the last one has the index returned by the function (a value of 0 is special in that it is the filename of the game executable, including the path).

Note that this function works on the HTML5 platform, retrieving the URL parameters.

 

#### Syntax:

parameter\_string(n)

 

#### Returns:

[String](../../GML_Overview/Data_Types.md)

 

#### Example:

var \_p\_num \= parameter\_count();  

 if (\_p\_num \> 0\)  

 {  

     for (var i \= 0; i \< \_p\_num; i\+\+)  

     {  

         p\_string\[i] \= parameter\_string(i \+ 1\);  

     }  

 }

The above code will get the number of command\-line parameters, and if there is 1 or more it will loop through them and store them as strings in an array.
