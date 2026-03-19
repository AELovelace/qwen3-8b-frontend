# camera\_get\_active

This function can be used to retrieve the unique camera ID value of the currently active camera.

The active camera is the camera used by GameMaker for drawing. It is set and changed by GameMaker during the various Draw events and can also change when you set a custom surface as the draw target using [surface\_set\_target](../../Drawing/Surfaces/surface_set_target.md) or when you call [camera\_apply](camera_apply.md) to apply a given camera.

  The active camera is only first set automatically during the first Draw event and the value returned by this function isn't necessarily valid outside of the Draw events.

 

#### Syntax:

camera\_get\_active()

 

#### Returns:

[Camera ID](camera_create.md)

 

#### Example:

var \_active \= camera\_get\_active();  

 if (\_active !\= view\_camera\[0])  

 {  

     view\_camera\[0] \= \_active;  

 }

The above code gets the camera ID for the active camera and sets the view camera for port\[0] to use it.
