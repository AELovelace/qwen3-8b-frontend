# Get View Variable

This action permits you to get the value of certain built\-in variables related to a given **viewport**. You select the viewport variable to retrieve, then give the viewport to target (from 0 to 7\) and finally the target variable to hold the returned value (this can be flagged as being a temporary local variable). The viewport is the area of the screen that will be used to draw a given camera view (as set up in [The Room Editor](../../../The_Asset_Editors/Rooms.md)), and the different variables that you are able to get in this way are outlined in the table below:

| Variable | Description |
| --- | --- |
| Camera | The value returned will be the unique ID value of the camera to assigned to the viewport (see [Cameras And Viewports](../../../GameMaker_Language/GML_Reference/Cameras_And_Display/Cameras_And_Viewports/Cameras_And_View_Ports.md) for more information). |
| Visibility | This will return a value of true or false where true indicates the viewport is visible (i.e.: it is being drawn to the screen), and false that nothing is being drawn. |
| Viewport X Coordinate | This is the X position of the viewport within the game window. |
| Viewport Y Coordinate | This is the Y position of the viewport within the game window. |
| Viewport Width | This is the width (in pixels) of the viewport. |
| Viewport Height | This is the height (in pixels) of the viewport. |
| Viewport Surface ID | This will return the handle for the surface assigned to the viewport or an invalid handle (\-1\) if no surface has been assigned. |

 

#### Action Syntax:

#### Arguments:

| Argument | Description |
| --- | --- |
| Variable | The built\-in view variable to get |
| View | The viewport to target (from 0 \- 7\) |
| Target | The target variable to hold the returned value (can be flagged as a temporary local variable) |

 

#### Example:

The above action block code gets the current camera ID assigned to viewport \[0] and then checks to see if it is the same as the one stored in a global variable. If it is not, the camera is set to the new one.
