# Set Gravity Force

This action is used to set the force of gravity acting on an instance. Each instance can have a different gravity force (and direction) independently of all others. The force applied is a value in pixels per game frame, and is cumulative, ie: it is
 added on each step, so if you have a speed of 2 and a gravity of 1, speed will increment by 1 each step, meaning that normally you'll want very low values here. Note that you can input negative values for gravity and the instance will be "pulled"
 in the opposite direction to the gravity direction.

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| force | The gravity force to apply (can be negative) |

 

#### Example:

The above action block code sets various instance properties related to movement:
 gravity direction is set to down (270°), gravity force is set to 0\.05, and friction is set to 0\.2\.
