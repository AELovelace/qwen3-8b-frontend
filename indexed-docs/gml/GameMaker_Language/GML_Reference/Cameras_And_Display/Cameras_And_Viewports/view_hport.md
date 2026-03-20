# view\_hport

This variable can be used to get or to set the height of the specified viewport. The height of the viewport (or combined viewports if more than one are active) define the height of the game window or background canvas *at the start of the game*, so changing this value after the game has started will have no visible effect on the game window size unless called along with the function [window\_set\_size](../The_Game_Window/window_set_size.md). If you have a larger or smaller viewport size than that assigned to the camera, then the camera view will be scaled down \- or up \- to fit, as illustrated by the image below.

 

 

#### Syntax:

view\_hport\[0 ... 7]

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

camera\_set\_view\_size(view\_camera\[0], view\_wport\[0], view\_hport\[0]);

The above code sets the width and height of the camera view to be the same as the width and height of the viewport.
