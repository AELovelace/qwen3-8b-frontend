# struct\_names\_count

This function gets the total number number of variables defined in a struct.

You supply the struct ID to check, and the function will return an integer value for the number of variables encountered, or (if no struct of the given ID exists) \-1\.

 

#### Syntax:

struct\_names\_count(struct\_id)

| Argument | Type | Description |
| --- | --- | --- |
| struct\_id | [Struct](../../GML_Overview/Structs.md) | The struct to check (can be the [global](../../GML_Overview/Variables/Global_Variables.md) struct) |

 

#### Returns:

[Real](../../GML_Overview/Data_Types.md)

 

#### Example:

var \_num \= struct\_names\_count(mystruct);  

 show\_debug\_message("Struct Variables \= " \+ string(\_num));

The above code will retrieve the number of variables in the given struct and show a debug message in the console output with this value.
