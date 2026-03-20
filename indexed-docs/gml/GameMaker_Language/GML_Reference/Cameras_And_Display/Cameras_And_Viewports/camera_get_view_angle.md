# camera\_get\_view\_angle

This function can be used to retrieve the angle of the given camera. The return value will be between 0 and 360\.

 
 

#### Syntax:

camera\_get\_view\_angle(camera\_id)

| Argument | Type | Description |
| --- | --- | --- |
| camera\_id | [Camera ID](camera_create.md) | The unique camera ID value returned when you created the camera |

 

#### Returns:

[Real](../../../GML_Overview/Data_Types.md)

 

#### Example:

var \_ang \= camera\_get\_view\_angle(view\_camera\[0]);  

 if (\_ang !\= 0\)  

 {  

     camera\_set\_view\_angle(view\_camera\[0], 0\);  

 }

The above code retrieves the angle of the camera assigned to viewport\[0] and then checks this to see if it matches the given value. If it does not then the view camera is set to that angle.
