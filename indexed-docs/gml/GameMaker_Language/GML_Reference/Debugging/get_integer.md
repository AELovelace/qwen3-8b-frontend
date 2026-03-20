# get\_integer

This creates a pop\-up window showing a custom message, with a button labelled "Ok", and prompts the user to input an integer value. The function will return the typed in integer, or the default value if nothing has been entered.

 
It is recommended to use [get\_integer\_async](../Asynchronous_Functions/Dialog/get_integer_async.md) instead as it can be used on more platforms and it is good practice to use asynchronous dialog windows.

 

#### Syntax:

get\_integer(str, def)

| Argument | Type | Description |
| --- | --- | --- |
| str | [String](../../GML_Overview/Data_Types.md) | The string to show in the pop\-up message. |
| def | [Real](../../GML_Overview/Data_Types.md) | The default value in the text box. |

 

#### Returns:

[Real](../../GML_Overview/Data_Types.md)

 

#### Example:

global.level \= get\_integer("Level to test?", 1\);

The above code will display a message prompting the user to select a level for testing. The return value will be stored in the global variable "global.level".
