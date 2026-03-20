# title

This action can be used to resume a previously paused sound. This can be used on any sound that has been paused using [Pause Audio](Pause_Audio.md) or [Pause All Audio](Pause_All_Audio.md), and will have no effect on those sounds
 that have not been paused previously.

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Sound | The sound resource to resume playing |

 

#### Example:

The above action block code will check a global variable and if it evaluates to true then
 the given sound is paused, otherwise it is resumed.
