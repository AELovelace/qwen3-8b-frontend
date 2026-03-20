# camera\_get\_view\_mat

This function returns the view matrix of the given camera.

The function returns the matrix which can then be used in other [Matrix Functions](../../Maths_And_Numbers/Matrix_Functions/Matrix_Functions.md) or to set the view matrix of another camera (using [camera\_set\_view\_mat](camera_set_view_mat.md)). Note that this function is generally for use with cameras created using [camera\_create](camera_create.md), but it can also be used on those created in the Room Editor (or with [camera\_create\_view](camera_create_view.md)) \- in which case the returned matrix will only be valid after the given camera is used in a viewport for the first time.

 

#### Syntax:

camera\_get\_view\_mat(camera\_id)

| Argument | Type | Description |
| --- | --- | --- |
| camera\_id | [Camera ID](camera_create.md) | The unique camera ID value returned when you created the camera |

 

#### Returns:

[Matrix](../../Maths_And_Numbers/Matrix_Functions/Matrix_Functions.md)

 

#### Example:

mat \= camera\_get\_view\_mat(view\_camera\[0]);

The above code gets the view matrix for the camera assigned to viewport\[0].
