# gc\_target\_frame\_time

With this function you can indicate to the garbage collector the amount of time it should aim to spend running each frame. The time value is specified in microseconds (where 1,000,000 microseconds equals one second) and the default target frame time is 100 microseconds.

Depending on the sign of the value, the garbage collector will run in a different "mode":

- If you pass a positive value, the garbage collector will aim to spend as little time as possible each frame on garbage collection, and no more than the amount of time specified.
- If you pass a negative value, the garbage collector will aim to spend as much time as possible each frame \- all remaining time in the frame if possible \- on garbage collection, and at least the amount of time specified.

Please note that this is simply a *target* value, as some operations still need to run completely in one frame and may sometimes take longer than the target time. Also note that increasing the target time will make the garbage collector more responsive to rapid changes in memory usage and will cause memory to be freed more quickly, though in practice this is unlikely to be required in most cases. Also note that setting the target frame time to 0 will *not* cause the collector to stop completely \- it will still do a minimal amount of work each frame.

To completely disable the collector use the [gc\_enable](gc_enable.md) function.

 

#### Syntax:

gc\_target\_frame\_time(time)

| Argument | Type | Description |
| --- | --- | --- |
| time | [Real](../../GML_Overview/Data_Types.md) | The target time \- in microseconds \- that the garbage collector should work each frame. Can be a positive value to indicate the maximum amount of time to spend, a negative value to indicate the minimum amount of time to spend. |

 

#### Returns:

N/A

 

#### Example 1: Positive Time Value

if (gc\_get\_target\_frame\_time() !\= 50\)  

 {  

     gc\_target\_frame\_time(50\);  

 }

The above code checks the current frame time target for the garbage collector and if it is not 50 microseconds then it is set to this value.

 

#### Example 2: Negative Time Value

gc\_target\_frame\_time(\-100\);

The above code sets the target frame time to a negative value. This tells the garbage collector to spend as much time as possible on garbage collection every frame, with at least 100 microseconds spent on it per frame, if possible (and if needed).
