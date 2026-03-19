# title

This action allows you to change the settings for an existing Time Source, specified in the "Time Source" field.

The settings supplied here are the same as [Create Time Source](Create_Time_Source.md), except for the parent.

It will reset and deactivate the Time Source so you have to start it again.

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Time Source | The [Time Source ID](../../../../GameMaker_Language/GML_Reference/Time_Sources/time_source_create.md) to reconfigure |
| Period | The period length of the Time Source, how long it takes to expire |
| Units | The [units](../../../GameMaker_Language/GML_Reference/Time_Sources/Time_Source_Units.md) that the period is expressed in (seconds or frames) |
| Callback | The [method](../../../GameMaker_Language/GML_Overview/Method_Variables.md) to call when the Time Source expires |
| Arguments | OPTIONAL An [array](../../../GameMaker_Language/GML_Overview/Arrays.md) containing the arguments to pass into the callback function |
| Repetitions | OPTIONAL How many times the Time Source should run in total, or \-1 for indefinite repetition |
| Expiry Type | OPTIONAL The [expiry type](../../../GameMaker_Language/GML_Reference/Time_Sources/Time_Source_Expiry_Types.md) for the Time Source |
