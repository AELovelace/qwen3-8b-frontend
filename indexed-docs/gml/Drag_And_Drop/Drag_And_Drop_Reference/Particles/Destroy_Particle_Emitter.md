# title

This action will "destroy" the given particle emitter, ie: free up the memory used by the particle emitter. You supply the particle system ID that the emitter belongs to (as returned by the action [Create Particle System](Create_Particle_System.md))
 and then the actual emitter ID (as returned by the action [Create Particle Emitter](Create_Particle_Emitter.md)). This action should be called whenever you no longer need a particle emitter in your game, or whenever you wish to re\-create
 the particle emitter (for example, just before calling a [Game Restart](../Game/Restart_Game.md)). Note that if the particle system the emitter has been assigned to has *not* been flagged as **Persistent** then you do *not need to call this action*,
 as the emitter will be automatically cleaned up on room end along with the particle system.

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| System | The ID value of the system that contains the emitter |
| Emitter | The ID value of the emitter to destroy |

 

#### Example:

The above action block code will check an instance variable and
 if it is over 100 it will destroy the emitter assigned to the instance and then go to the next room.
