# camera\_set\_default

This function can be used to set the default camera to use a custom camera that you have previously created using one of the [camera\_create](camera_create.md) functions.

When you create a room with *no* active viewports or view cameras, GameMaker still uses a camera to show the action in the game. This camera is called the **default** camera and can be set, manipulated and even destroyed just like any other camera.

 

#### Syntax:

camera\_set\_default(camera\_id)

| Argument | Type | Description |
| --- | --- | --- |
| camera\_id | [Camera ID](camera_create.md) | The unique camera ID value returned when you created the camera |

 

#### Returns:

N/A

 

#### Example:

var \_new\_cam \= camera\_create\_view(0, 0, 640, 480, 0, obj\_player, 5, 5, \-1, \-1\);  

 camera\_set\_default(\_new\_cam);

The above code creates a new camera and then assigns it as the default camera to use.
