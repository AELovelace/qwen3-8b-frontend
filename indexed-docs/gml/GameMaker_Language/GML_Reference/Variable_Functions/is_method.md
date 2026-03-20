# is\_method

This function can be used to check and see if a variable is a method variable (it will return true) or not (in which case it will return false).

  To check if a value is callable (i.e. refers to a method or a function), see [is\_callable](is_callable.md).

#### Syntax:

is\_method(n)

| Argument | Type | Description |
| --- | --- | --- |
| n | [Any](../../../../GameMaker_Language/GML_Overview/Data_Types.md#variable) | The variable to check. |

 

#### Returns:

[Boolean](../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

if is\_method(get\_vec)  

 {  

     show\_debug\_message("Method variable!");  

 }

The above code checks a variable to see if it is a method, and if the function returns true, then a debug message is output to the console.
