# variable\_get\_hash

This function returns a hash for the given string. This hash can be used with the [struct\_get\_from\_hash](struct_get_from_hash.md) and [struct\_set\_from\_hash](struct_set_from_hash.md) functions.

 
 

#### Syntax:

variable\_get\_hash(name)

| Argument | Type | Description |
| --- | --- | --- |
| name | [String](../../GML_Overview/Data_Types.md) | The name of the variable to get the hash from |

 

#### Returns:

[Real](../../GML_Overview/Data_Types.md)

 

#### Example:

var \_the\_struct \= {a: 77, b: 88, c: 99};  

 var \_varname \= choose("a", "b", "c");  

 var \_hash \= variable\_get\_hash(\_varname);  

 var \_value \= struct\_get\_from\_hash(\_the\_struct, \_hash);

The above code creates a temporary struct \_the\_struct with three member variables: a, b and c. It then calls [choose](../Maths_And_Numbers/Number_Functions/choose.md) to pick one of these variable names at random and uses the returned name in variable\_get\_hash to get that variable name's hash. This hash is stored in a temporary variable \_hash and then used in [struct\_get\_from\_hash](struct_get_from_hash.md) to retrieve the value of the struct member with the corresponding name. The returned value is assigned to another temporary variable \_value.
