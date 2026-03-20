# struct\_get\_from\_hash

This function gets the value of a struct member using the hash returned by [variable\_get\_hash](variable_get_hash.md).

 
 

#### Syntax:

struct\_get\_from\_hash(struct, hash)

| Argument | Type | Description |
| --- | --- | --- |
| struct | [Struct](../../GML_Overview/Structs.md) | The struct reference to use |
| hash | [Real](../../GML_Overview/Data_Types.md) | The hash of the variable to get (as returned by [variable\_get\_hash](variable_get_hash.md)) |

 

#### Returns:

[Any](../../GML_Overview/Data_Types.md#variable)

 

#### Example:

var \_the\_struct \= {a: 77, b: 88, c: 99};  

 var \_hash \= variable\_get\_hash("a");  

 var \_value \= struct\_get\_from\_hash(\_the\_struct, \_hash);

The above code creates a temporary struct \_the\_struct with three member variables: a, b and c. It then gets the hash of a variable a. This hash is then used in struct\_get\_from\_hash to retrieve the value of the struct member with the corresponding name. The returned value is assigned to another temporary variable \_value.
