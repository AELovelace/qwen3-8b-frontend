# struct\_get

This function gets the value from a given named variable within a struct.

You supply the struct reference as well as the name of the variable to get the value of *as a string* (see example code below). The function will return the value held by the variable or undefined if the named variable does not exist.

  If the variable you are getting does not exist then the function will return the keyword undefined and you may get errors that will stop the game from functioning, so if in doubt use the function [struct\_exists](variable_struct_exists.md) first.

 

#### Syntax:

struct\_get(struct, name)

| Argument | Type | Description |
| --- | --- | --- |
| struct | [Struct](../../GML_Overview/Structs.md) | The struct reference to use (can be the [global](../../GML_Overview/Variables/Global_Variables.md) struct) |
| name | [String](../../GML_Overview/Data_Types.md) | The name of the variable to get (as a string) |

 

#### Returns:

[Any](../../GML_Overview/Data_Types.md#variable) (any data type) or [undefined](../../GML_Overview/Data_Types.md) (if the named variable does not exist)

 

#### Example:

if (struct\_exists(mystruct, "shields"))  

 {  

     var ss \= struct\_get(mystruct, "shields");  

 }  

 else  

 {  

     var ss \= \-1;  

 }

The above code will check to see if a variable exists in the given struct and if it does then the value it holds is retrieved and stored in a local variable. If it does not exist, the local variable is set to \-1\.
