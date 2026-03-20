# is\_handle

This function checks if the supplied value is a handle. It returns true if it is, otherwise it returns false.

Read about handles on the page for [Data Types](../../GML_Overview/Data_Types.md).

 

#### Syntax:

is\_handle(val)

| Argument | Type | Description |
| --- | --- | --- |
| val | [Any](../../GML_Overview/Data_Types.md#variable) | The value to check. |

 

#### Returns:

[Boolean](../../GML_Overview/Data_Types.md)

 

#### Example:

var \_handle \= sprite\_index;  

  

 var \_is\_handle \= is\_handle(\_handle);  

 var \_is\_handle\_text \= \_is\_handle ? "holds" : "doesn't hold";  

  

 show\_debug\_message($"The variable \_handle {\_is\_handle\_text} a handle!");
 

The above code checks a variable \_handle to see if it holds a handle and outputs the result in a debug message.
