# Time Source States

| [Time Source State Constant](../../../../GameMaker_Language/GML_Reference/Time_Sources/Time_Source_States.md) | | |
| --- | --- | --- |
| Constant | Description | Value |
| time\_source\_state\_initial | The Time Source has not been started yet | 0 |
| time\_source\_state\_active | The Time Source has been [started](time_source_start.md) and is counting down | 1 |
| time\_source\_state\_paused | The Time Source is [paused](time_source_pause.md) | 2 |
| time\_source\_state\_stopped | The Time Source was [stopped](time_source_stop.md) or it completely expired | 3 |

A Time Source can have a state, which can be any one of the constants above. The default state for a newly\-created Time Source is time\_source\_state\_initial.

The state can be changed using [time\_source\_start()](time_source_start.md), [time\_source\_stop()](time_source_stop.md), and [time\_source\_pause()](time_source_pause.md).

The state of a Time Source is returned using [time\_source\_get\_state()](time_source_get_state.md).
