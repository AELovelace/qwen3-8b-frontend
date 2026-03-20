# date\_inc\_month

With this function you can increment a given datetime value by a specific number of months, and it will return the new datetime value.

 

#### Syntax:

date\_inc\_month( date, amount )

| Argument | Type | Description |
| --- | --- | --- |
| date |  | The datetime to add to. |
| amount |  | The number of months (must be an integer) to add. |

 

#### Returns:

 

#### Example:

mynewdatetime \= date\_inc\_month(date\_current\_datetime(), 12\);

This would set "mynewdatetime" to the current date but with 12 months added.
