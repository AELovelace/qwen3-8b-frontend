# get\_string

This creates a pop\-up window showing a standard message, with a button labelled "Ok", that prompts the user to input a string. The function will return the input string, *or* the default value if nothing has been entered.

 
It is recommended to use [get\_string\_async](../Asynchronous_Functions/Dialog/get_string_async.md) instead as it can be used on more platforms and it is good practice to use asynchronous dialog windows.

 

#### Syntax:

get\_string(str, def)

| Argument | Type | Description |
| --- | --- | --- |
| str | [String](../../GML_Overview/Data_Types.md) | The string to show in the pop\-up message. |
| def | [String](../../GML_Overview/Data_Types.md) | The default string in the text box. |

 

#### Returns:

[String](../../GML_Overview/Data_Types.md)

 

#### Example:

global.test\_name \= get\_string("Test highscore name:", "Anonymous");

The above code will prompt the user to give a name which will then be stored in the global variable "test\_name". If nothing is entered and the user just presses "Ok" then the default value, "Anonymous", will be returned.
