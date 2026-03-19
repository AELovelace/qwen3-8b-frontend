# date\_inc\_week

With this function you can increment a given datetime value by a specific number of weeks, and it will return the new datetime value.

 

#### Syntax:

date\_inc\_week(date, amount)

| Argument | Type | Description |
| --- | --- | --- |
| date |  | The datetime to add to. |
| amount |  | The number of weeks (must be an integer) to add. |

 

#### Returns:

 

#### Example:

mynewdatetime \= date\_inc\_week(date\_current\_datetime(), 52\);

This would set mynewdatetime to the current date but with 52 weeks added.
