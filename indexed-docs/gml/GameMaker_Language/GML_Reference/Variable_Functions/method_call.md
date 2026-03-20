# method\_call

This function calls a [method](../../GML_Overview/Method_Variables.md) in its bound context, with the arguments taken from an array or a range in an array.

The array\_args parameter is optional and can be omitted if the method takes no arguments. If the parameter is provided, the range of elements can optionally be specified using the offset and num\_args parameters.

  You can use [script\_execute\_ext](../Asset_Management/Scripts/script_execute_ext.md) to call a method in the context of the calling instance or struct instead of the bound context of the method.

 

#### Syntax:

method\_call(method, \[array\_args], \[offset], \[num\_args])

| Argument | Type | Description |
| --- | --- | --- |
| method | [Method](../../GML_Overview/Method_Variables.md) | The method to call |
| array\_args | [Array](../../GML_Overview/Arrays.md) | The array containing the arguments to pass into the method |
| offset | [Real](../../GML_Overview/Data_Types.md) | The offset, or starting index, in the array. The item at this array index is the *first* argument for the method. Defaults to 0\.  Setting a negative value will count from the end of the array. The starting index will then be array\_length(array\_args) \+ offset. See: [Offset And Length](Array_Functions.md#offset_and_length) |
| num\_args | [Real](../../GML_Overview/Data_Types.md) | The number of elements to pass as arguments. A negative value will traverse the array backwards (i.e. in descending order of indices, e.g. 2, 1, 0 instead of 2, 3, 4\). See: [Offset And Length](Array_Functions.md#offset_and_length) |

 

#### Returns:

[Any](../../GML_Overview/Data_Types.md#variable) (the type returned by the method)

 

#### Example:

struct\_with\_a\_method \=   

 {  

     show\_message: function(message)  

     {  

         show\_debug\_message("The message is: {0}", message);  

     }  

 }  

 var \_method \= struct\_with\_a\_method.show\_message;  

method\_call(\_method, \["Hello World!"]);
 

The above code first defines a struct struct\_with\_a\_method that has a method show\_message. The method is then assigned to a temporary variable \_method. Next it is called using method\_call with an argument array with 1 item in it: the string "Hello World!". The show\_message function calls [show\_debug\_message](../Debugging/show_debug_message.md) which outputs "The message is: Hello World!".
