# struct\_remove

This function removes a variable from a struct. You supply the struct ID to remove the variable from and the string name of the variable to be removed.

 

#### Syntax:

struct\_remove(struct, name)

| Argument | Type | Description |
| --- | --- | --- |
| struct | [Struct](../../GML_Overview/Structs.md) | The struct reference to remove the variable from |
| name | [String](../../GML_Overview/Data_Types.md) | The name of the variable to remove (as a string) |

 

#### Returns:

N/A

 

#### Example:

if (struct\_exists(mystruct, "shields"))   

 {  

     struct\_remove(mystruct, "shields");  

 }

The above code will check to see if the given variable exists in the given struct and if it does then it is removed.
