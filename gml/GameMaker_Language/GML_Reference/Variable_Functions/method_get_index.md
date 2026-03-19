# method\_get\_index

This function gives you the [Script Function](../../GML_Overview/Script_Functions.md) reference for the given method. This can be used to retrieve the original function behind a method bound to an instance or a struct.

When an invalid value is passed (e.g. not a method), this returns undefined.

 

#### Syntax:

method\_get\_index(method)

| Argument | Type | Description |
| --- | --- | --- |
| method | [Method](../../GML_Overview/Method_Variables.md) | The method variable to check |

 

#### Returns:

[Script Function](../../GML_Overview/Script_Functions.md)

 

#### Example:

var \_index \= method\_get\_index(light\_setup);  

 if (\_index !\= undefined)  

 {  

     show\_debug\_message(script\_get\_name(\_index));  

 }

The above code will get the function index for the method light\_setup and then if it is not undefined it will output the function's name to the console.
