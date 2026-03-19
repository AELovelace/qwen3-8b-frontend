# vector\_sprite\_cache\_prune\_age

This function sets how long entries in the cache must not have been used before being deleted by the automatic pruning logic. This value is measured in frames and should be 0 or greater. The default is 1800 (30 seconds if the game is running at 60fps).

 

#### Syntax:

vector\_sprite\_cache\_prune\_age(frames)

| Argument | Type | Description |
| --- | --- | --- |
| frames | [Real](../../../../GML_Overview/Data_Types.md) | The number of frames an entry in the cache must not have been used before being deleted |

 

#### Returns:

N/A

 

#### Example:

vector\_sprite\_cache\_prune\_age(600\);

The code above sets the prune age to 600 frames, or 10 seconds at a game speed of 60fps.
