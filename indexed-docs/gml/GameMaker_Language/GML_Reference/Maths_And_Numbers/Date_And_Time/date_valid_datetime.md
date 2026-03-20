# date\_valid\_datetime

With this function you can check a datetime value to see if it is valid (returns true) or not (returns false).

Note that this function will only consider a valid datetime as being *after* 1/1/1970 and anything before that will return false, so the earliest you can check would be:

date\_valid\_datetime(1970, 01, 01, 0, 0, 0\);

 

#### Syntax:

date\_valid\_datetime(year, month, day, hour, minute, second)

| Argument | Type | Description |
| --- | --- | --- |
| year | [Real](../../../GML_Overview/Data_Types.md) | The year to check |
| month | [Real](../../../GML_Overview/Data_Types.md) | The month to check |
| day | [Real](../../../GML_Overview/Data_Types.md) | The day to check |
| hour | [Real](../../../GML_Overview/Data_Types.md) | The hour to check |
| minute | [Real](../../../GML_Overview/Data_Types.md) | The minute to check |
| second | [Real](../../../GML_Overview/Data_Types.md) | The second to check |

 

#### Returns:

[Boolean](../../../GML_Overview/Data_Types.md)

 

#### Example:

if (date\_valid\_datetime(2011, 9, 15, 10, 3, 30\))  

 {  

     mydatetime \= date\_create\_datetime(2011, 9, 15, 10, 3, 30\);  

 }

This will set mydatetime to 15th September 2011, 10:03\.30, if it is a valid value (which it is).
