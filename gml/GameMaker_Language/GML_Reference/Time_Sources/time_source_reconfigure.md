# time\_source\_reconfigure

This function is used to modify the core properties of a Time Source, without having to create an entirely new one.

You specify an existing Time Source, and then set the properties that are also set in [time\_source\_create()](time_source_create.md), except the parent. Read that page for detailed information on these properties.

The specified Time Source will be reset and deactivated, and will need to be [started](time_source_start.md) again.

 

#### Syntax:

time\_source\_reconfigure(id, period, units, callback, \[args], \[repetitions], \[expiry\_type])

| Argument | Type | Description |
| --- | --- | --- |
| id | [Time Source](time_source_create.md) | The Time Source to reconfigure |
| period | [Real](../../GML_Overview/Data_Types.md) | The period that the Time Source runs for, in the given units |
| units | [Time Source Unit Constant](Time_Source_Units.md) | The units that the given period is in |
| callback | [Method](../../GML_Overview/Method_Variables.md) | The method to call when the Time Source expires |
| args | [Array](../../GML_Overview/Arrays.md) | An array containing the arguments to pass into the method. The default is an empty array. |
| repetitions | [Real](../../GML_Overview/Data_Types.md) | The number of times the Time Source should repeat, or \-1 for indefinite repetition. The default value is 1\. |
| expiry\_type | [Time Source Expiry Constant](Time_Source_Expiry_Types.md) | Whether the Time Source expires on the frame nearest to its expiry, or on the next frame. The default value is time\_source\_expire\_after. |

 

#### Returns:

N/A

 

#### Example:

function change\_spawn\_delay(new\_delay)  

 {  

     time\_source\_reconfigure(obj\_game.spawn\_time\_source, new\_delay, time\_source\_units\_frames, obj\_game.spawn\_method, \[], \-1\);  

     time\_source\_start(obj\_game.spawn\_time\_source);  

 }

This creates a new function that changes the spawn delay used for in\-game enemies.

Assuming the game uses a Time Source called obj\_game.spawn\_time\_source to spawn enemies, that Time Source will need to be updated once the spawn delay changes.

This function does exactly that, reconfiguring the Time Source with the new delay and then [starting it](time_source_start.md) again.
