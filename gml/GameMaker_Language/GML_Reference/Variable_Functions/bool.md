# bool

This function will attempt to convert a given value into a boolean data type, where the value will be returned as true if it is greater than 0\.5, and false otherwise.

 

#### Syntax:

bool(n)

| Argument | Type | Description |
| --- | --- | --- |
| n | [Real](../../GML_Overview/Data_Types.md) | The value to convert. |

 

#### Returns:

[Boolean](../../GML_Overview/Data_Types.md)

 

#### **Example:**

if (!is\_bool(val))  

 {  

     val \= bool(val);  

 }

The above code checks the variable val to see if it is a boolean and if it's not converts it to one.
