# gc\_enable

With this function you can enable or disable the garbage collector. Calling the function with true as the argument enables it and using false disables it (not recommended). It is enabled by default.

 

#### Syntax:

gc\_enable(enable)

| Argument | Type | Description |
| --- | --- | --- |
| enable | [Boolean](../../GML_Overview/Data_Types.md) | Whether to enable (true) or disable (false) the garbage collector |

 

#### Returns:

N/A

 

#### Example:

if (global.debug \=\= true)  

 {  

     gc\_enable(false);  

 }

The above code disables garbage collection if the given global variable is true.
