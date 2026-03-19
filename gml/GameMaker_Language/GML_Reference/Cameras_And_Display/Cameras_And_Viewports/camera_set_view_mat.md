# camera\_set\_view\_mat

This function sets the **view matrix** for a given camera. You give the unique camera ID value (as returned by the different [camera\_create](camera_create.md) functions) and a view matrix to be applied. You can find out more about creating view matrices from the section [Matrix Functions](../../Maths_And_Numbers/Matrix_Functions/Matrix_Functions.md), specifically [matrix\_build\_lookat](../../Maths_And_Numbers/Matrix_Functions/matrix_build_lookat.md).

Note that if your camera does automatic object tracking \- i.e.: it has been created using [camera\_create\_view](camera_create_view.md) with an object index / instance ID that isn't \-1, or you are setting a camera defined in the Room Editor, or you are setting the default camera \- then this matrix will get overwritten the next game frame.

 

#### Syntax:

camera\_set\_view\_mat(camera\_id, matrix)

| Argument | Type | Description |
| --- | --- | --- |
| camera\_id | [Camera ID](camera_create.md) | The unique camera ID value returned when you created the camera |
| matrix | [Matrix](../../Maths_And_Numbers/Matrix_Functions/Matrix_Functions.md) | The unique matrix ID returned when you created the matrix |

 

#### Returns:

N/A

 

#### Example:

view\_camera\[0] \= camera\_create();  

 var \_viewmat \= matrix\_build\_lookat(640, 240, \-10, 640, 240, 0, 0, 1, 0\);  

 var \_projmat \= matrix\_build\_projection\_ortho(640, 480, 1\.0, 32000\.0\);  

 camera\_set\_view\_mat(view\_camera\[0], \_viewmat);  

 camera\_set\_proj\_mat(view\_camera\[0], \_projmat);

The above code creates a new camera and assigns it to viewport\[0]. This camera then has its view and projection matrices set.
