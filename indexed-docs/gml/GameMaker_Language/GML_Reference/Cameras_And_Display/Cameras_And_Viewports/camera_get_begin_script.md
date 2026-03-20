# camera\_get\_begin\_script

This function can be used to retrieve the ID of the [script function](../../../GML_Overview/Script_Functions.md) assigned as the begin script for the given camera. If no script function is assigned then the function will return an invalid handle (\-1\).

 

#### Syntax:

camera\_get\_begin\_script(camera\_id)

| Argument | Type | Description |
| --- | --- | --- |
| camera\_id | [Camera ID](camera_create.md) | The unique camera ID value returned when you created the camera |

 

#### Returns:

 

 

#### Example:

var \_scr \= camera\_get\_begin\_script(view\_camera\[0]);  

 if (\_scr !\= cutscene)  

 {  

     camera\_set\_begin\_script(view\_camera\[0], cutscene);  

 }

The above code checks the script function assigned as the begin script for the camera assigned to viewport\[0] and if it is not cutscene it is set to that function.
