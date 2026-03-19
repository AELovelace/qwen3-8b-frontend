# is\_undefined

This function checks whether a given value is equal to the value undefined or not. In some cases you want to check and see what data type a variable holds in GameMaker and that's when you would use this function. It returns true or false depending on whether the value is undefined or not.

  This function **cannot** be used to verify the existence of a variable. Use [variable\_instance\_exists](variable_instance_exists.md) or [variable\_global\_exists](variable_global_exists.md) instead.

 

#### Syntax:

is\_undefined(n)

| Argument | Type | Description |
| --- | --- | --- |
| n | [Any](../../GML_Overview/Data_Types.md#variable) | The argument to check |

 

#### Returns:

[Boolean](../../GML_Overview/Data_Types.md)

 

#### **Example:**

var \_val \= ds\_map\_find\_value(map, 13\);  

 if (is\_undefined(\_val))  

 {  

     show\_debug\_message("Map entry does not exist!");  

 }

The above code checks the variable \_val to see if it is undefined or not and shows a debug message if it is.
