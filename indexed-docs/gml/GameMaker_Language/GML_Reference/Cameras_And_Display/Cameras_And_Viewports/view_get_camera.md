# view\_get\_camera

This function can be used to retrieve the unique camera ID value for the camera assigned to the given viewport (from 0 \- 7\). If no camera is assigned, the function will return \-1\.

 

#### Syntax:

view\_get\_camera(viewport)

| Argument | Type | Description |
| --- | --- | --- |
| viewport | [Real](../../../GML_Overview/Data_Types.md) | The viewport to target (0 \- 7\) |

 

#### Returns:

[Camera ID](camera_create.md)

 

#### Example:

var \_cam \= view\_get\_camera(0\);  

 var \_cw \= camera\_get\_view\_width(cam);  

 var \_ch \= camera\_get\_view\_height(cam);  

 camera\_set\_view\_pos(\_cam, mouse\_x \- (\_cw / 2\), mouse\_y \- (\_ch / 2\));

The above code will retrieve the camera ID for the camera assigned to viewport\[0] and then change its position.
