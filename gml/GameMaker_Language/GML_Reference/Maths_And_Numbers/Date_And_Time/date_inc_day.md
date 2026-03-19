# date\_inc\_day

With this function you can increment a given datetime value by a specific number of days, and it will return the new datetime value.

 

#### Syntax:

date\_inc\_day(date, amount)

| Argument | Type | Description |
| --- | --- | --- |
| date |  | The datetime to add to. |
| amount |  | The number of days (must be an integer) to add. |

 

#### Returns:

 

#### Example:

mynewdatetime \= date\_inc\_day(date\_current\_datetime(), 365\);

This would set "mynewdatetime" to the current date but with 365 days added.
