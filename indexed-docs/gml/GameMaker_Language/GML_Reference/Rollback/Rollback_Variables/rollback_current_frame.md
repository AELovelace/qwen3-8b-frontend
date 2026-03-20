# rollback\_current\_frame

This is a global variable that stores the number of frames that have passed since the multiplayer game was started.

This should be used instead of [current\_time](../../Maths_And_Numbers/Date_And_Time/current_time.md) and other similar variables, as explained in [Time Variables](../Rollback_Constraints.md#h).

 

#### Syntax:

rollback\_current\_frame

 

#### Returns:

[Real](../../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

image\_angle \= dsin(rollback\_current\_frame) \* 90;

The code above uses rollback\_current\_frame with [dsin()](../../Maths_And_Numbers/Angles_And_Distance/dsin.md) to calculate an oscillating value between 1 and \-1, which is multiplied by 90 and applied to the instance's angle.
