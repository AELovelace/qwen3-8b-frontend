# ptr

This function will attempt to convert a given value into a pointer data type, where the value *must* be either a real, a string, an int64, an int32, or a ptr. Anything else will cause the game to crash with an error message.

 

#### Syntax:

ptr(n)

| Argument | Type | Description |
| --- | --- | --- |
| n | [Real](../../../../GameMaker_Language/GML_Overview/Data_Types.md), [String](../../../../GameMaker_Language/GML_Overview/Data_Types.md), or [Pointer](../../../../GameMaker_Language/GML_Overview/Data_Types.md) | The value to convert. |

 

#### Returns:

[Pointer](../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### **Example:**

if (!is\_ptr(val))   

 {  

     val \= ptr(application\_surface);  

 }

The above code checks the variable "val" to see if it contains a pointer and if it does not then one is assigned to it.
