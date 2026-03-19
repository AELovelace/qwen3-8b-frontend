# title

With this action you can set the volume for the whole sound system. The volume value you give can be between 0 (silent) and 1 (full volume) and the scale is linear, such that a value of 0\.5 would be half volume. Note that this action will affect all
 instances of all sounds that are playing currently in the room, and will affect all future instances of all sounds played. This action is also independent of the volume set for any individual sound, so if you have a sound set to play at 0\.5 volume
 and then set the master volume to 0\.5, the sound will play at 0\.25 volume.

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Volume | The new master volume for all sound (from 0 to 1, default 1\) |

 

#### Example:

The above action block code checks a global variable to see if it is true or
 false. If it is true then the master volume for the sound system is retrieved and stored in a temporary local variable. The value is then checked to see if it is not equal to 0\.5, and if it is not, then the master volume of the sound system
 is set to 0\.5\. If the global variable evaluates to false, then the master volume is set to 1\.
