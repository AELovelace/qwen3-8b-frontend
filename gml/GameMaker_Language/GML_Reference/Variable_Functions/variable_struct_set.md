# struct\_set

With this function you can set the value of a given variable in a struct. You supply the struct reference as well as the name of the variable to set the value of *as a string* (see example code below), and then finally the value to set (can be any valid [data type](../../GML_Overview/Data_Types.md)). If the variable does not exist already in the struct it will be created and then assigned the value.

 

#### Syntax:

struct\_set(struct, name, val)

| Argument | Type | Description |
| --- | --- | --- |
| struct | [Struct](../../GML_Overview/Structs.md) | The struct reference to set (can be the [global](../../GML_Overview/Variables/Global_Variables.md) struct) |
| name | [String](../../GML_Overview/Data_Types.md) | The name of the variable to set (as a string, must not be empty) |
| val | [Any](../../GML_Overview/Data_Types.md#variable) | The value to set the variable to |

 

#### Returns:

N/A

 

#### Example:

if (!struct\_exists(mystruct, "shields"))  

 {  

     struct\_set(mystruct, "shields", 0\);  

 }

The above code will check to see if the given variable exists in the given struct and if it does not then it is created and set to 0\.
