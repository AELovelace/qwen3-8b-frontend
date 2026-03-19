# Snap Position

This action is used to "snap" an instance to a specific grid coordinate position. You supply the size of the grid "cell" and the instance will be snapped to that grid, for example, if you set the grid snap values for horizontal and vertical to 8, and the instance is at (4, 6\), then it will be snapped to the position (0, 8\) \- essentially the current position is rounded to the nearest value divisible by the horizontal and vertical snap settings where the grid cells start at the top left corner of the room (0, 0\). The default values are set to a snap of (32, 32\) but you can change them to whatever positive integer value you require.

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| horizontal | The horizontal cell value to snap to |
| vertical | The vertical cell value to snap to |

 

#### Example:

The above action block code checks for the mouse left button being held down on the instance, and if it is then the instance follows the mouse and when the button is released, the instance is snapped to a 32 by 32 grid.
