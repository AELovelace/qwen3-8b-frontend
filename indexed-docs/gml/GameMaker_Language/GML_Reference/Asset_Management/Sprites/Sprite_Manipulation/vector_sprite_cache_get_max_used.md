# vector\_sprite\_cache\_get\_max\_used

This function returns the maximum amount of memory (in bytes) which has been used by the vector sprite cache. This value is reset if the cache size is changed by [vector\_sprite\_cache\_limit](vector_sprite_cache_limit.md).

 

#### Syntax:

vector\_sprite\_cache\_get\_max\_used()

 

#### Returns:

[Real](../../../../GML_Overview/Data_Types.md)

 

#### Example:

var \_used \= vector\_sprite\_cache\_get\_max\_used();

The code above gets the maximum amount of memory used by the vector sprite cache and stores it in a temporary variable.
