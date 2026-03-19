# title

This action can be used to check whether an instance of any sound resource is currently paused in your game. You give the sound resource to check for from the asset explorer and the function will return true if it is paused and false
 if it is not, although if you check the "not" flag, this is reversed and the function will return true if the sound is *not* paused and false otherwise.

Note that to add actions into the "if" block, they should be dropped to the side of the action, as shown in the image below:

These actions will now be run if the "if" evaluates to true, while
 any actions dropped elsewhere will be performed after the "if" block.

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Sound | The sound resource to check |

 

#### Example:

The above action block code checks to see if the given sound is currently paused and
 if it is, it resumes playing it.
