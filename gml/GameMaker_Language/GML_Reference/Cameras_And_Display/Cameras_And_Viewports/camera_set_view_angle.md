# camera\_set\_view\_angle

You can use this function to update the angle of the view camera within the room. You give the unique camera ID value (as returned by the different [camera\_create](camera_create.md) functions) and then give the angle that you wish to set the camera view to. The default value is 0° with positive values rotating the camera **counterclockwise**, i.e.: setting the value to 90 will rotate the camera 90° to the left.

 

#### Syntax:

camera\_set\_view\_angle(camera\_id, angle)

| Argument | Type | Description |
| --- | --- | --- |
| camera\_id | [Camera ID](camera_create.md) | The unique camera ID value returned when you created the camera |
| angle | [Real](../../../GML_Overview/Data_Types.md) | The new angle to set the camera view to |

 

#### Returns:

N/A

 

#### Example:

camera\_set\_view\_angle(view\_camera\[0], point\_direction(x, y, mouse\_x, mouse\_y));

The above code will set the view camera angle for the camera assigned to viewport\[0].
