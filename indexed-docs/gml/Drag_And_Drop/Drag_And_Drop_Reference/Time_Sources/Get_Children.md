# title

This action returns an array containing all the child Time Sources for the given Time Source.

The resulting array is stored in the Target variable.

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Time Source | The [Time Source ID](../../../../GameMaker_Language/GML_Reference/Time_Sources/time_source_create.md) to get the children of |
| Target | The variable to store the array |
| Temp | Whether the variable should be created as a temporary variable |

 

#### Example:

  

 This gets the children for a Time Source, and loops through the array to destroy each child Time Source.

At the end it destroys the parent Time Source.
