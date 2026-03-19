# Load Game

This action will load a game that has previously been saved using the [Save Game](Save_Game.md) action.

You give the filename of the file to load (as a string, and including the extension) and the game will be loaded and continue running from the saved point. Note that this is not designed as a universal save/load system, and trying to load a game saved from a previous run of the project may give errors (especially if you have used things like [Data Structures](../Data_Structures/Data_Structure_Actions.md) or [Particles](../Particles/Particle_Actions.md)), and as such you should only try and load games that have been saved in the progress of a single game play\-through (for things like checkpoints). Also note that the file will *not* be loaded until the end of the current event or script, so any actions after the load action is called will still be performed.

 
 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Timeline | The timeline resource to assign to an instance |

 

#### Example:

The above action block code will check a global variable and if it is less than or equal to 0 it will load a previously saved game.
