# show\_message

This function creates a pop\-up message box which displays the given string and a button marked "Ok" to close it.

 
It is recommended to use [show\_message\_async](../Asynchronous_Functions/Dialog/show_message_async.md) instead as it can be used on more platforms and it is good practice to use asynchronous dialog windows.

 

#### Syntax:

show\_message(str)

| Argument | Type | Description |
| --- | --- | --- |
| str | [String](../../GML_Overview/Data_Types.md) | The string to show in the pop\-up message. |

 

#### Returns:

N/A

 

#### Example:

var tot \= 0;  

 for (var i \= 0; i \< 10; i \+\= 1\)  

 {  

     tot \+\= inv\[i];  

 }  

 show\_message("Total \= " \+ string(tot));

The above code will loop through the values stored in the array "inv" and add them to the variable "tot" before showing a message with the total.
