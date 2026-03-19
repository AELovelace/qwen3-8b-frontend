# ds\_queue\_read

With this function you can recreate a saved DS queue (one that has previously been written as a string using [ds\_queue\_write()](ds_queue_write.md)). You must first create a new DS queue to read the string into, and if the DS queue already exists and has information stored in it, then this will be cleared before reading. This function is of vital importance when creating save/load mechanisms for your game.

 
 

#### Syntax:

ds\_queue\_read(id, str \[, legacy])

| Argument | Type | Description |
| --- | --- | --- |
| id | [DS Queue](ds_queue_create.md) | The handle of the data structure to read into. |
| str | [String](../../../GML_Overview/Data_Types.md) | The string to read from. |
| legacy | [Boolean](../../../GML_Overview/Data_Types.md) | Can be either true or false or omitted completely. |

 

#### Returns:

N/A

 

#### Example:

queue \= ds\_queue\_create();  

 ini\_open("save.ini");  

 var str \= ini\_read\_string("Queues", "0", "");  

 if (str !\= "")  

 {  

     ds\_queue\_read(queue, str);  

 }  

 ini\_close();

The above code creates a queue and stores the index in the variable "queue". It then opens an ini file and reads a string from that, checking to make sure that the string is not returned as empty first. This string is then read into the newly created DS queue.
