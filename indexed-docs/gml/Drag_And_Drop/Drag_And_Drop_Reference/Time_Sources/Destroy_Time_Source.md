# title

This action destroys the given Time Source.

You cannot destroy a Time Source if it has existing [children](Get_Children.md). Destroy the child Time Sources first before destroying a parent ([example](Get_Children.md)).

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Time Source | The [Time Source ID](../../../../GameMaker_Language/GML_Reference/Time_Sources/time_source_create.md) to destroy |

 

#### Example:

  

 This checks if a Time Source exists, and if it does, it destroys it.
