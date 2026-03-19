# is\_struct

This function checks if the supplied value is a struct. It returns true if it is, otherwise it returns false.

Note that [method variables](../../GML_Overview/Method_Variables.md) will also return true, and [object instances](../Asset_Management/Instances/Instances.md) will return false.

 

#### Syntax:

is\_struct(val)

| Argument | Type | Description |
| --- | --- | --- |
| val | [Any](../../../../GameMaker_Language/GML_Overview/Data_Types.md#variable) | The value to check. |

 

#### Returns:

[Boolean](../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

if (is\_struct(a))   

 {  

     delete(a);  

 }

The above code checks a variable to see if it is a struct, and if the function returns true, the struct is deleted.
