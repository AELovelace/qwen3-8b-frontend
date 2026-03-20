# title

This action sets the "seed" for the random number generator to a random value. When using the random number functions in GameMaker the initial seed is always the same, as this makes tracing errors and debugging far easier (compiled
 games do not have this behaviour). Should you wish to test with true random, you should call this action once at the start of the game.

 

#### Action Syntax:

 

#### Example:

The above action block code sets the random seed to a new value then generates a number from 0
 to 9 and assigns it to a global scope variable.
