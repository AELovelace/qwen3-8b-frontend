# date\_date\_string

With this function you can create a string containing the given date, formatted as day/month/year.

 

#### Syntax:

date\_date\_string(date)

| Argument | Type | Description |
| --- | --- | --- |
| date |  | The date to use. |

 

#### Returns:

 

#### Example:

str \= date\_date\_string(date\_current\_datetime());  
 draw\_text(32, 32, str);

This would set "str" to hold a formatted string of the current date and time as shown by the system.
