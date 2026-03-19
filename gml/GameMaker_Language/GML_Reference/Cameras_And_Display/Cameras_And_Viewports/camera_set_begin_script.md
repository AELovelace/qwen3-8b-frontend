# camera\_set\_begin\_script

This function can be used to set a function that will be called at the beginning of every game frame that the camera is assigned to a visible and active viewport.

You give the unique camera ID value (as returned by the different [camera\_create](camera_create.md) functions) and the function to be called.  

 
 

#### Syntax:

camera\_set\_begin\_script(camera\_id, script)

| Argument | Type | Description |
| --- | --- | --- |
| camera\_id | [Camera ID](camera_create.md) | The unique camera ID value returned when you created the camera |
| script |  | The function to run each game frame (or \-1 for no begin script) |

 

#### Returns:

N/A

 

#### Example:

camera\_set\_begin\_script(view\_camera\[0], beginCamera);

The above code sets the begin script function for the camera assigned to viewport \[0].
