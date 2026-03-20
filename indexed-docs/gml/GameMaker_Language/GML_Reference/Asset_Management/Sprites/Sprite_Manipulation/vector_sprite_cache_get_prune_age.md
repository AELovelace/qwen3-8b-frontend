# vector\_sprite\_cache\_get\_prune\_age

This function returns the number of frames an entry in the vector sprite cache can exist without being used before it is considered for deletion.

 

#### Syntax:

vector\_sprite\_cache\_get\_prune\_age()

 

#### Returns:

[Real](../../../../GML_Overview/Data_Types.md)

 

#### Example:

var \_age \= vector\_sprite\_cache\_get\_prune\_age();

The code example gets the current prune age for entries in the vector sprite cache and stores it in a temporary variable.
