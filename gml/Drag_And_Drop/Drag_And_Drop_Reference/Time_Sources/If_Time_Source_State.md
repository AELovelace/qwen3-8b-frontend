# title

This action allows you to control other actions based on the state of the given Time Source.

It checks if the [Time Source State Constant](../../../../GameMaker_Language/GML_Reference/Time_Sources/Time_Source_States.md) given in "State" is (or isn't) the state of the Time Source given in "Time Source".

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Time Source | The [Time Source ID](../../../../GameMaker_Language/GML_Reference/Time_Sources/time_source_create.md) to check the state of |
| Not | Enable this to invert the condition |
| State | The [Time Source State Constant](../../../../GameMaker_Language/GML_Reference/Time_Sources/Time_Source_States.md) to check against |

 

#### Example:

  

 This code block would ideally run in a Key Press event.

It checks if the state of a Time Source is "active", and in that case, it pauses that Time Source.

However, if the state is "paused", it starts the Time Source again.
