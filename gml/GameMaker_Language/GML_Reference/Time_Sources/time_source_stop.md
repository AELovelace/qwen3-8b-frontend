# time\_source\_stop

This function stops the given Time Source and resets its timer. You cannot stop a Time Source that has either not started, or is in a finished state.

 

#### Syntax:

time\_source\_stop(id)

| Argument | Type | Description |
| --- | --- | --- |
| id | [Time Source ID](../../../../GameMaker_Language/GML_Reference/Time_Sources/time_source_create.md) | The Time Source to stop |

 

#### Returns:

N/A

 

#### Example:

if (time\_source\_get\_state(time\_source) !\= time\_source\_state\_stopped)  

 {  

     time\_source\_stop(time\_source);  

 }

The code above will stop a Time Source when it's not already stopped.
