# argument

This variable acts as an [array](../../Arrays.md) that is used along with the read\-only variable [argument\_count](argument_count.md) in [script functions](../../Script_Functions.md) or [methods](../../Method_Variables.md). Each index holds an input value for the function and is specifically for use with *variable* argument functions (i.e. where the number of arguments can vary between calls).

An argument that hasn't been passed in will be undefined.

Note that there are also a series of independent global scope variables that can also be used in user\-defined functions to reference the different input arguments: argument0, argument1, argument2, etc. up to argument15.

 
 

#### Syntax:

argument\[n]  

 argument1  

 argument2  

 ...  

 argument15

 

#### Returns:

[Any](../../Data_Types.md#variable) (can be of any data type supplied to the function)

 

#### Example:

function print()  

 {  

     var \_str \= "";  

     for (var i \= 0; i \< argument\_count; i \+\+)  

     {  

         \_str \+\= string(argument\[i]);  

     }  

     show\_debug\_message(\_str);  

 }  

  

 // In an object  

 print("Player : ", current\_time, " : ", id, " : fired");
 

The above function joins all the arguments passed into the function into one string, and then prints that string to the output log.
