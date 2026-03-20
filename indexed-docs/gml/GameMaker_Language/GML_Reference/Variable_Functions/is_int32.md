# is\_int32

This function returns whether a given variable is a 32bit integer or not.

In some cases you want to check and see what data type a variable holds in GameMaker and that's when you would use this function. It returns true or false depending on whether the value is an int32 or not.

 

#### Syntax:

is\_int32(n)

| Argument | Type | Description |
| --- | --- | --- |
| n | [Any](../../GML_Overview/Data_Types.md#variable) | The argument to check. |

 

#### Returns:

[Boolean](../../GML_Overview/Data_Types.md)

 

#### **Example:**

if (!is\_int32(val))   

 {  

     show\_debug\_message("Not a 32 bit integer!");  

 }

The above code checks the variable "val" to see if it contains an int32 and if it is not then it shows a message in the debug console.
