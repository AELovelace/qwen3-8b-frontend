# title

This action returns the volume of the given sound. You pick the sound from the asset explorer and give a target variable to return the volume value to (you can flag this as being a temporary local variable). The returned value will be between 0 and
 1, where 0 is silent and 1 is full volume.

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Sound | The sound resource to get the volume of |
| Target | The target variable to store the returned volume |

 

#### Example:

The above action block code checks a global variable to see if it is true or false. If it is true then the volume of the given sound is retrieved and stored in a temporary local variable. The value is then checked to see if it is not equal to 0\.5, and if it is not, then the volume of the sound is set to 0\.5\. If
 the global variable evaluates to false, then the sound has its volume set to 1\.
