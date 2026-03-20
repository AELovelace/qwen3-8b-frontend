# camera\_get\_proj\_mat

This function returns the projection matrix of the given camera. The function returns the matrix which can then be used in other [Matrix Functions](../../Maths_And_Numbers/Matrix_Functions/Matrix_Functions.md) or to set the projection matrix of another camera (using [camera\_set\_proj\_mat](camera_set_proj_mat.md)).

 

#### Syntax:

camera\_get\_proj\_mat(camera\_id)

| Argument | Type | Description |
| --- | --- | --- |
| camera\_id | [Camera ID](camera_create.md) | The unique camera ID value returned when you created the camera |

 

#### Returns:

[Matrix](../../Maths_And_Numbers/Matrix_Functions/Matrix_Functions.md)

 

#### Example:

mat \= camera\_get\_proj\_mat(view\_camera\[0]);

The above code gets the projection matrix for the camera assigned to viewport\[0].
