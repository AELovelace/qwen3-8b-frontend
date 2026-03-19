# date\_get\_timezone

This function gets the base time zone being used for all the rest of the date and time functions, which can be either *local* (as set by the system) or *UTC*.

The function will return one of the following constants:

| [Time Zone Constant](date_get_timezone.md) | |
| --- | --- |
| Constant | Description |
| timezone\_local | use the local time zone as set by the system |
| timezone\_utc | use Coordinated Universal Time |

 

#### Syntax:

date\_get\_timezone()

 

#### Returns:

[Time Zone Constant](date_get_timezone.md)

 

#### Example:

if (date\_get\_timezone() !\= timezone\_utc)  

 {  

     date\_set\_timezone(timezone\_utc);  

 }

This code checks the base time zone setting for the game and if it is not UTC it then changes it.
