# title

This action will "destroy" the given particle type created by the action [Create Particle Type](Create_Particle_Type.md) (ie: free up the memory used by the particle type). This action should be called whenever you no longer need
 a particle type in your game, or whenever you wish to re\-create the particle type (for example, just before calling a [Game Restart](../Game/Restart_Game.md)).

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Type | The ID value for the type to destroy |

 

#### Example:

The above action block code will check for the "Space" key
 being pressed and if it is detected then it removes the particle system and different particle types defined in the given global variables and then restarts the game.
