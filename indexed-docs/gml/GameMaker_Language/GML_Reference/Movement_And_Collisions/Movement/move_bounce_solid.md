# move\_bounce\_solid

With this function you can command an instance to bounce off only those instances marked as **solid** within the room. You can also tell it to use precise collision checking when enabled, but be aware that this requires all instances to have precise
 masks enabled and will greatly slow down your game when many instances are involved due to the amount of processing that has to be done. This should normally go in the step event of an instance, but can be used selectively in a collision event too.

 

#### Syntax:

move\_bounce\_solid(adv)

| Argument | Type | Description |
| --- | --- | --- |
| adv |  | Whether to enable advanced bouncing (true) or not (false). |

 

#### Returns:

 

#### Example:

move\_bounce\_solid(false);

This will enable non\-precise bouncing off instances flagged as "solid".
