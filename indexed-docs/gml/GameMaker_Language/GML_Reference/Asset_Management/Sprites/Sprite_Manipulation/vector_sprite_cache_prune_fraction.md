# vector\_sprite\_cache\_prune\_fraction

This function sets what fraction of the cache is attempted to be cleared each frame. This can be a value between 0\.0 and 1\.0 (a value of 0\.0 will disable automatic pruning). This will only attempt to clear cache entries that are older than the number of frames specified by [vector\_sprite\_cache\_prune\_age](vector_sprite_cache_prune_age.md). The default value is 0\.01\.

 

#### Syntax:

vector\_sprite\_cache\_prune\_fraction(fraction)

| Argument | Type | Description |
| --- | --- | --- |
| fraction | [Real](../../../../GML_Overview/Data_Types.md) | A value from 0\.0 to 1\.0 that indicates the fraction of the cache to prune |

 

#### Returns:

N/A

 

#### Example:

vector\_sprite\_cache\_prune\_fraction(0\.08\);

The code above sets the vector sprite cache fraction to prune to 0\.08\.
