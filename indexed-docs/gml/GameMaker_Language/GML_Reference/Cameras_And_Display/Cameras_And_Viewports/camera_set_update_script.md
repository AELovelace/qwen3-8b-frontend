# camera\_set\_update\_script

This function can be used to set a function that will be called every game frame that the camera is assigned to a visible and active viewport.

You give the unique camera ID value (as returned by the different [camera\_create](camera_create.md) functions) and the function to be called.  

 
  Applying a custom update function to a camera overrides its default update behaviour. For example, if you set your camera to follow an object (say, obj\_player) when calling [camera\_create\_view](camera_create_view.md), or set it so in the [Room Properties](../../../../The_Asset_Editors/Room_Properties/Room_Properties.md), it will stop following that object once a custom update script is set.

 

#### Syntax:

camera\_set\_update\_script(camera\_id, script)

| Argument | Type | Description |
| --- | --- | --- |
| camera\_id | [Camera ID](camera_create.md) | The unique camera ID value returned when you created the camera |
| script |  | The function to run each game frame (or \-1 for no update script) |

 

#### Returns:

N/A

 

#### Example:

camera\_set\_update\_script(view\_camera\[0], updateCamera);

The above code sets the update function for the camera assigned to viewport \[0].
