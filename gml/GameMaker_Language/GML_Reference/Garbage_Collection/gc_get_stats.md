# gc\_get\_stats

With this function you can retrieve information about the current state of the garbage collector. The function will return a [struct](../../GML_Overview/Structs.md) which will have the following member variables (note that "objects" here refers to anything that can be garbage collected and *not* general object instances as defined in the Asset Browser):

| [GC Stats Struct](gc_get_stats.md) | | |
| --- | --- | --- |
| Variable | Type | Description |
| objects\_touched | [Real](../../GML_Overview/Data_Types.md) | This is the number of active objects the garbage collector found in the previous frame. This will vary depending on which generation was collected. |
| objects\_collected | [Real](../../GML_Overview/Data_Types.md) | The number of objects which the garbage collector determined weren't active in the previous frame, and which could therefore be deleted. |
| traversal\_time | [Real](../../GML_Overview/Data_Types.md) | This is the time in microseconds (on the main thread) which the garbage collector took to figure out which objects were active. |
| collection\_time | [Real](../../GML_Overview/Data_Types.md) | This is the time in microseconds (on a separate thread) which the garbage collector took to clean up the objects deemed inactive. |
| gc\_frame | [Real](../../GML_Overview/Data_Types.md) | This is a counter which is incremented every time a garbage collection pass occurs. If garbage collection is disabled this will not increase. |
| generation\_collected | [Real](../../GML_Overview/Data_Types.md) | This is the index of the generation that was collected last. 0 is the youngest generation and 3 is currently the oldest. |
| num\_generations | [Real](../../GML_Overview/Data_Types.md) | This is the total number of garbage collection generations. |
| num\_objects\_in\_generation | [Array](../../GML_Overview/Arrays.md) of [Real](../../GML_Overview/Data_Types.md)s | This is an array (of size num\_generations) containing the number of objects in each generation. |

  On the HTML5 target platform garbage collection is handled by the JavaScript engine and therefore the member variables in the above struct will all hold 0 if this function is used on that platform.

When using this function, please note that the information shown for the objects *is only updated when a full generation is finished processing*, which may take several frames depending on frame time setting (see [here](gc_target_frame_time.md) for more information on frame timing).

 

#### Syntax:

gc\_get\_stats()

 

#### Returns:

[GC Stats Struct](gc_get_stats.md)

 

#### Example:

if (global.debug \=\= true)  

 {  

     var \_s \= gc\_get\_stats();  

     var \_t \= \_s.traversal\_time;  

     var \_c \= \_s.collection\_time;  

     show\_debug\_message("Traversal time \= " \+ string(\_t));  

     show\_debug\_message("Collection time \= " \+ string(\_c));  

 }

The above code checks a global variable and if it is true it gets information from the garbage collector and outputs it to the console as debug messages.
