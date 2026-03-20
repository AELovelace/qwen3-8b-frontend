# date\_hour\_span

With this function you can get the number of hours between two dates. This value is always positive, and incomplete hours will be returned as a fraction.

 

#### Syntax:

date\_hour\_span(date1, date2\)

| Argument | Type | Description |
| --- | --- | --- |
| date1 |  | The first datetime. |
| date2 |  | The datetime to compare the first one to. |

 

#### Returns:

 

#### Example:

diff \= date\_hour\_span(date\_create\_datetime( 2011, 9, 15, 11, 4, 0 ), date\_current\_datetime());

This would set "diff" to the number of hours between 15th September 2011, 11:04\.0 and the current date and time.
