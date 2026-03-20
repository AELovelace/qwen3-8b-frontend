# ds\_priority\_read

With this function you can recreate a saved DS priority (one that has previously been written as a string using [ds\_priority\_write()](ds_priority_write.md)). You must first create a new DS priority to read the string into, and if the DS priority already exists and has information stored in it, then this will be cleared before reading. This function is of vital importance when creating save/load mechanisms for your game.

 
 

#### Syntax:

ds\_priority\_read(id, str, \[legacy])

| Argument | Type | Description |
| --- | --- | --- |
| id | [DS Priority](ds_priority_create.md) | The handle of the data structure to write. |
| str | [String](../../../GML_Overview/Data_Types.md) | The string to read from. |
| legacy | [Boolean](../../../GML_Overview/Data_Types.md) | Can be either true or false or omitted completely. |

 

#### Returns:

N/A

 

#### Example:

p\_queue \= ds\_priority\_create();  

 ini\_open("save.ini");  

 var str \= ini\_read\_string("P\_Queues", "0", "");  

 if (str !\= "")  

 {  

     ds\_priority\_read(p\_queue, str);  

 }  

 ini\_close();

The above code creates a priority queue and stores the index in the variable "p\_queue". It then opens an ini file and reads a string from that, checking to make sure that the string is not returned as empty first. This string is then read into the newly created DS priority.
