# date\_inc\_second

With this function you can increment a given datetime value by a specific number of seconds, and it will return the new datetime value.

 

#### Syntax:

date\_inc\_second(date, amount)

| Argument | Type | Description |
| --- | --- | --- |
| date |  | The datetime to add to. |
| amount |  | The number of seconds (must be an integer) to add. |

 

#### Returns:

 

#### Example:

mynewdatetime \= date\_inc\_second(date\_current\_datetime(), 60\);

This would set "mynewdatetime" to the current date but with 60 seconds added.
