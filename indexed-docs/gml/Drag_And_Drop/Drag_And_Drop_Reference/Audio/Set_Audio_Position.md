# title

With this action you can set a sound to start from a specific time.

You give the sound to play, and the time to start it from, but this action will *not* play the sound for you, it will simply set the play position for the sound. To use this action you must *first* set the position *then* play the sound using the action [Play Audio](Play_Audio.md), otherwise you will here no change in position until the next time you play the same sound resource (which will start at the new position).

The position is set in seconds \- you can use decimal values \- and you can get the total sound length using the action [Get Audio Length](Get_Audio_Length.md).

Values beyond the end of the sound are clamped to its length.

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Sound | The sound resource to set the play position of |
| Time | The time to set (in seconds) |

 

#### Example:

The above action block code gets the playing length of the given sound resource and stores it in a temporary local variable. This is then used to generate a random value between 0 and the length of the sound, which is then stored in a different temporary local variable. This new random value is then used to set the start position for the sound and the sound is then played.
