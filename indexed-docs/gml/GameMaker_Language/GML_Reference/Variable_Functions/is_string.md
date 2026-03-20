# is\_string

This function returns whether a given variable is a string or not.

In some cases you want to check and see if a variable in GameMaker holds a string and not a real and that's when you would use this function. It does *not* return the string but rather true or false, so a value of, for example, "fish" for n will return true, but a value of 200 for n will return false.

 

#### Syntax:

is\_string(n)

| Argument | Type | Description |
| --- | --- | --- |
| n | [Any](../../GML_Overview/Data_Types.md#variable) | The argument to check. |

 

#### Returns:

[Boolean](../../GML_Overview/Data_Types.md)

 

#### **Example:**

if (is\_string(val))  

 {  

     name \= "Player: " \+ val;  

 }

The above code checks the variable "val" to see if it contains a string and if it does it adds it into another string which is then assigned to the variable "name".
