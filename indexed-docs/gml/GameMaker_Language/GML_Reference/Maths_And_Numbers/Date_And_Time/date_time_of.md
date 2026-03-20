# date\_time\_of

This function returns the time value of the given datetime.

The time returned ignores Daylight Saving Time (and so is Universal Time) and would normally be used in conjunction with another date/time handling function.

 

#### Syntax:

date\_time\_of(date)

| Argument | Type | Description |
| --- | --- | --- |
| date | [Datetime](date_current_datetime.md) | The datetime to extract the time from. |

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

time \= date\_time\_of(date\_current\_datetime());

This would return the current time only and store the value in the variable "time".
