# title

This action can be used to pause the chosen sound if it is currently playing. Note if you have played multiple instances of the same sound, *all* of them will be paused, and this does not pause any sounds played *after* the action has been
 called. You can start a paused sound playing again using the action [Resume Audio](Resume_Audio.md).

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Sound | The sound resource to pause |

 

#### Example:

The above action block code will check a global variable and if it evaluates to true then
 the given sound is paused, otherwise it is resumed.
