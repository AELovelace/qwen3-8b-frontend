# time\_source\_destroy

This function will destroy the given Time Source. You can optionally specify whether all child Time Sources under it should be deleted as well.

You cannot use this function to destroy the time\_source\_global and time\_source\_game [Built\-In Time Sources](Built_In_Time_Sources.md). You can, however, use this to delete all the child Time Sources under them, meaning the second argument destroy\_tree must be true when passing a built\-in Time Source.

 

#### Syntax:

time\_source\_destroy(id, \[destroy\_tree])

| Argument | Type | Description |
| --- | --- | --- |
| id | [Time Source](time_source_create.md) | The Time Source to destroy |
| destroy\_tree | [Boolean](../../GML_Overview/Data_Types.md) | OPTIONAL Whether to destroy child Time Sources as well, is false by default |

 

#### Returns:

N/A

 

#### Example:

// Create event  

 time\_source \= time\_source\_create(time\_source\_game, 1, time\_source\_units\_seconds, my\_method, \[], \-1\);  

  

 // Clean Up event  

 time\_source\_destroy(time\_source);
 

The Create event code creates a new Time Source that expires once per second and repeats indefinitely.

The Clean Up event code destroys that Time Source, as it will not be needed after the instance is destroyed.
