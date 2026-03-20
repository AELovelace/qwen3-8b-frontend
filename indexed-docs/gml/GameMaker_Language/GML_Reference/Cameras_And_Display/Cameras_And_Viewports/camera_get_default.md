# camera\_get\_default

This function can be used to retrieve the unique camera ID value of the default camera (the camera that GameMaker uses when no camera views or viewports are active in a game room).

 

#### Syntax:

camera\_get\_default()

 

#### Returns:

[Camera ID](camera_create.md)

 

#### Example:

var \_def \= camera\_get\_default();  

 view\_camera\[0] \= \_def;

The above code gets the camera ID for the default camera and sets the view camera for port\[0] to use it.
