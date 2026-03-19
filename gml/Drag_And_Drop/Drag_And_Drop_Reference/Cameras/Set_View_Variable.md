# Set View Variable

This action permits you to set certain built\-in variables related to how the **viewport** will display camera views of the room. You select the viewport variable to edit, then give the viewport to target (from 0 to 7\) and finally the new value for the variable. The viewport is the area of the screen that will be used to draw a given camera view (as set up in [The Room Editor](../../../The_Asset_Editors/Rooms.md)), and the different variables that you are able to set in this way are outlined in the table below:

| Variable | Description |
| --- | --- |
| Camera | This is for setting the viewport to show a different Camera View. You need to supply the unique ID value of the camera to change to (see [Cameras And Viewports](../../../GameMaker_Language/GML_Reference/Cameras_And_Display/Cameras_And_Viewports/Cameras_And_View_Ports.md) for more information). |
| Visibility | This is the visibility toggle for the viewport and expects a value of true or false , where setting it to true will make the viewport visible (i.e.: it will draw to the screen), and a value of false will not draw anything to the screen. |
| Viewport X Coordinate | This is the X position of the viewport within the game window. Note though that is is only really required when more than one viewport is active \- for example to create a split screen effect \- and if used when only one viewport is active you get unexpected results. |
| Viewport Y Coordinate | This is the Y position of the viewport within the game window. Note though that is is only really required when more than one viewport is active \- for example to create a split screen effect \- and if used when only one viewport is active you get unexpected results. |
| Viewport Width | This is the width (in pixels) of the viewport. The width of the viewport (or combined viewports if more than one are active) defines the width of the game window or background canvas at the start of the game, so changing this value after the game has started *will have no visible effect on the game window size* unless called along with the GML function [window\_set\_size](../../../GameMaker_Language/GML_Reference/Cameras_And_Display/The_Game_Window/window_set_size.md). Also note that if you have a larger or smaller viewport size than that assigned to the camera, then the camera view will be scaled down \- or up \- to fit. |
| Viewport Height | This is the height (in pixels) of the viewport. The height of the viewport (or combined viewports if more than one are active) defines the height of the game window or background canvas at the start of the game, so changing this value after the game has started *will have no visible effect on the game window size* unless called along with the GML function [window\_set\_size](../../../GameMaker_Language/GML_Reference/Cameras_And_Display/The_Game_Window/window_set_size.md). Also note that if you have a larger or smaller viewport size than that assigned to the camera view, then the camera view will be scaled down \- or up \- to fit. |
| Viewport Surface ID | With this variable you can set the contents of a given viewport to draw to a surface, with the value you supply being that of the surface to use for drawing the viewport to. For more information please see [view\_surface\_id](../../../GameMaker_Language/GML_Reference/Cameras_And_Display/Cameras_And_Viewports/view_surface_id.md). |

 

#### Action Syntax:

#### Arguments:

 

| Argument | Description |
| --- | --- |
| Variable | The built\-in view variable to set |
| View | The viewport to target (from 0 \- 7\) |
| Value | The new value for the built\-in variable |

 

#### Example:

The above action block code will check for a key press and if one is detected it will make the viewport \[0] visible, otherwise it will make it invisible.
