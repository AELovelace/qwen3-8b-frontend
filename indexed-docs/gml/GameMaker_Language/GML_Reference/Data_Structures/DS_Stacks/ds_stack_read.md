# ds\_stack\_read

With this function you can recreate a saved DS stack (one that has previously been written as a string using [ds\_stack\_write()](ds_stack_write.md)). You must first create a new DS stack to read the string into, and if the DS stack already exists and has information stored in it, then this will be cleared before reading. This function is of vital importance when creating save/load mechanisms for your game.

 
 

#### Syntax:

ds\_stack\_read(id, str \[, legacy])

| Argument | Type | Description |
| --- | --- | --- |
| id | [DS Stack](ds_stack_create.md) | The handle of the data structure to read into. |
| str | [String](../../../GML_Overview/Data_Types.md) | The string to read from. |
| legacy | [Boolean](../../../GML_Overview/Data_Types.md) | Can be either true or false or omitted completely. |

 

#### Returns:

N/A

 

#### Example:

stack \= ds\_stack\_create();  

 ini\_open("save.ini");  

 var str \= ini\_read\_string("Stacks", "0", "");  

 if (str !\= "")  

 {  

     ds\_stack\_read(stack, str);  

 }  

 ini\_close();

The above code creates a stack and stores the index in the variable "stack". It then opens an ini file and reads a string from that, checking to make sure that the string is not returned as empty first. This string is then read into the newly created DS stack .
