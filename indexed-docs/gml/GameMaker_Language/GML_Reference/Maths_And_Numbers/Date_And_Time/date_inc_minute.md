# date\_inc\_minute

With this function you can increment a given datetime value by a specific number of minutes, and it will return the new datetime value.

 

#### Syntax:

date\_inc\_minute( date, amount )

| Argument | Type | Description |
| --- | --- | --- |
| date |  | The datetime to add to. |
| amount |  | The number of minutes (must be an integer) to add. |

 

#### Returns:

 

#### Example:

mynewdatetime \= date\_inc\_minute(date\_current\_datetime(), 60\);

This would set "mynewdatetime" to the current date but with 60 minutes added.
