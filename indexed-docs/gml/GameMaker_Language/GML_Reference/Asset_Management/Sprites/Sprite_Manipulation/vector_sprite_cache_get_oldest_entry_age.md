# vector\_sprite\_cache\_get\_oldest\_entry\_age

This function returns how long ago (in frames) the oldest entry in the vector sprite cache was last used. This can be useful for determining if the cache is set to an appropriate size.

 

#### Syntax:

vector\_sprite\_cache\_get\_oldest\_entry\_age()

 

#### Returns:

[Real](../../../../GML_Overview/Data_Types.md) (\-1 if there is no such entry)

 

#### Example:

var \_oldest\_age \= vector\_sprite\_cache\_get\_oldest\_entry\_age();  

 show\_debug\_message($"The oldest entry in the vector sprite cache was used {\_oldest\_age} frames ago.");

The code above gets the age of the oldest entry in the cache and assigns it to a temporary variable, then outputs it in a debug message.
