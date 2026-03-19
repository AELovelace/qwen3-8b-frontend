# date\_second\_span

With this function you can get the number of seconds between two dates. The return value is always positive and will be a whole number.

 

#### Syntax:

date\_second\_span(date1, date2\)

| Argument | Type | Description |
| --- | --- | --- |
| date1 |  | The first datetime. |
| date2 |  | The datetime to compare it to. |

 

#### Returns:

 

#### Example:

diff \= date\_second\_span(date\_create\_datetime(2011, 9, 15, 11, 4, 0 ), date\_current\_datetime());

This would set "diff" to the number of seconds between 15th September 2011, 11:04 and the current date and time.
