# date\_compare\_time

With this function you can check two dates and times to see which one has the time component earlier or later than the other. The function returns \-1 if datetime1 is earlier, 1 if datetime1 is later and 0 if they are the same, and it ignores the date,
 so literally just which of the times is further through its given day.

 

#### Syntax:

date\_compare\_time(datetime1, datetime2\)

| Argument | Type | Description |
| --- | --- | --- |
| datetime1 |  | The first datetime. |
| datetime2 |  | The datetime to compare the first one to. |

 

#### Returns:

 

#### Example:

d \= date\_compare\_time(date\_create\_datetime( 2011, 9, 15, 11, 4, 0 ), date\_current\_datetime());

This would set "d" to the corresponding value depending on which of the times was the earliest. Basically, if the current time is later than 11:04 am, it would return 1\. If earlier, \-1\. If the time is 11:04, it would return 0\.
