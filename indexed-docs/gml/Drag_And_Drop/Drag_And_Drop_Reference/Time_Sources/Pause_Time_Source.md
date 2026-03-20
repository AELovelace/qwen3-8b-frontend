# title

This action pauses the given Time Source.

You can resume it later using [Start Time Source](Start_Time_Source.md).

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Time Source | The [Time Source ID](../../../../GameMaker_Language/GML_Reference/Time_Sources/time_source_create.md) to pause |

 

#### Example:

  

 This code block would ideally run in a Key Press event.

It checks if the state of a Time Source is "active", and in that case, it pauses that Time Source.

However, if the state is "paused", it resumes the Time Source.
