# Save Game

This action will do a basic save of the game to a given file.

You give a filename (as a string and including the extension) and the action will perform a limited save out of the current game state. It's important to understand that the action is designed to take a "snapshot" of the current game state and is for use more as a checkpoint system than a universal save system, since it does *not* save any of the dynamic resources (like [Data Structures](../Data_Structures/Data_Structure_Actions.md) or [Particles](../Particles/Particle_Actions.md)). As such the action should be used very carefully so as not to get errors or memory leaks.

 
 

#### Action Syntax:

#### Arguments:

 

| Argument | Description |
| --- | --- |
| Filename | The name \- as a string and with the extension \- to give the file being saved (if the file already exists, it will be overwritten) |

 

#### Example:

The above action block code will check for a collision with another instance and if one is found it checks an instance variable. If the variable returns true then the game is saved and the variable set to false.
