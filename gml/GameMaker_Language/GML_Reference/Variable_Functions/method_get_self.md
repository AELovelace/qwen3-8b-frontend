# method\_get\_self

This function retrieves the instance or struct reference which is the [self](../../GML_Overview/Instance_Keywords.md) context used when the method is called. If the variable is *not* a method then the function will return undefined.

 

#### Syntax:

method\_get\_self(method)

| Argument | Type | Description |
| --- | --- | --- |
| method | [Method](../../GML_Overview/Method_Variables.md) | The method variable to check. |

 

#### Returns:

[Object Instance](../Asset_Management/Instances/Instance_Variables/id.md), [Struct](../../GML_Overview/Structs.md), or [undefined](../../GML_Overview/Data_Types.md)

 

#### Example:

var \_self \= method\_get\_self(light\_properties);  

 show\_debug\_message(string(\_self));

The above code gets the self context for the given method variable and outputs it to the console.
