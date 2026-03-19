# ds\_priority\_write

This function returns a string which can then be stored or transferred to another data structure using the [ds\_priority\_read()](ds_priority_read.md) function.

 
 

#### Syntax:

ds\_priority\_write(id)

| Argument | Type | Description |
| --- | --- | --- |
| id | [DS Priority ID](GameMaker_Language/GML_Reference/Data_Structures/DS_Priority_Queues/ds_priority_create.md) | The handle of the data structure to check. |

 

#### Returns:

[String](GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

var str;
   

 ini\_open("save.ini");
   

 str \= ds\_priority\_write(p\_queue);
   

 ini\_write\_string("P\_Queues", "0", str);
   

 ds\_priority\_clear(p\_queue);
   

 ini\_close();

The above code opens an ini file and then writes a string containing the information stored in the DS priority queue indexed in the variable "p\_queue". The priority queue is then cleared and the ini file closed.
