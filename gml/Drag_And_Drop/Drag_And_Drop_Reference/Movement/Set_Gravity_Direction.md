# Set Gravity Direction

This action is used to set the direction of the built\-in gravity variable. Each instance can have its own gravity effect, and if the gravity value is set to anything other than zero, then the instance will be "pulled" in the direction set by this action. You can set a direction between 0° and 360° where right is 0°, up is 90°, left is 180° and down is 270°. Note that you can set this to be relative to the current gravity value, so whatever you input will be added/subtracted from that.

 

#### Action Syntax:

#### Arguments:

 

| Argument | Description |
| --- | --- |
| direction | Direction from 0° to 360° (values outside of the range will be wrapped). |

 

#### Example:

The above action block code sets various instance properties related to movement: gravity direction is set to down (270°), gravity force is set to 0\.05, and friction is set to 0\.2\.
