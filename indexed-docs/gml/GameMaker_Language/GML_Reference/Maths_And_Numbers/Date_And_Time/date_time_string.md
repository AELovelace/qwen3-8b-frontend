# date\_time\_string

With this function you can create a string containing the given time, formatted for the system or device that is running the game when the function is called.

 

#### Syntax:

date\_time\_string(date)

| Argument | Type | Description |
| --- | --- | --- |
| date | [Datetime](date_current_datetime.md) | The datetime to use. |

 

#### Returns:

[String](../../../GML_Overview/Data_Types.md)

 

#### Example:

str \= date\_time\_string(date\_current\_datetime());

This would set the given variable to something like "11:36\.00" depending on the system settings for date/time displaying and the current date and time.
