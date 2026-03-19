# texture\_debug\_messages

This function enables or disables texture debug messages.

When enabled (set to true), additional information about texture page use will be sent to the output window. Set to false to disable this output again.

 

#### Syntax:

texture\_debug\_messages(enable)

| Argument | Type | Description |
| --- | --- | --- |
| enable | [Boolean](../../../GML_Overview/Data_Types.md) | Enable or disable the texture debug messages |

 

#### Returns:

N/A

 

#### Example:

if (global.debug)   

 {  

     texture\_debug\_messages(true);  

 }

The above code will check the value of a global variable and if it is set to true then texture debug messages are enabled.
