# date\_set\_timezone

This function sets the base time zone to use for all the rest of the date and time functions, which can either be *local* (as set by the system) or *UTC*.

You would use one of the following constants to define which is being used (by default this is local time):

| Constant | Description |
| --- | --- |
| timezone\_local | Use the local time zone as set by the system (the default option) |
| timezone\_utc | Use Coordinated Universal Time |

 

#### Syntax:

date\_set\_timezone(timezone)

| Argument | Type | Description |
| --- | --- | --- |
| timezone | [Time Zone Constant](date_get_timezone.md) | The time zone to use for the base time |

 

#### Returns:

N/A

 

#### Example:

if (date\_get\_timezone() !\= timezone\_utc)  

 {  

     date\_set\_timezone(timezone\_utc);  

 }

This code checks the base time zone setting for the game and if it is not UTC it then changes it.
