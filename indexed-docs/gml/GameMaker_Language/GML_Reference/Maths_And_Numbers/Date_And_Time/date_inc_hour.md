# date\_inc\_hour

With this function you can increment a given datetime value by a specific number of hours, and it will return the new datetime value.

 

#### Syntax:

date\_inc\_hour(date, amount)

| Argument | Type | Description |
| --- | --- | --- |
| date |  | The datetime to add to. |
| amount |  | The number of hours (must be an integer) to add. |

 

#### Returns:

 

#### Example:

mynewdatetime \= date\_inc\_hour(date\_current\_datetime(), 24\);

This would set mynewdatetime to the current date but with 24 hours added.
