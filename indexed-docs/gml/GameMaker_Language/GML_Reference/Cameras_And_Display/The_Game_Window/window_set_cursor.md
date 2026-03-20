# window\_set\_cursor

With this function you can set the cursor for the game window to any one of the constants listed below (to find the current cursor being used you can use the function [window\_get\_cursor()](../The_Game_Window/window_get_cursor.md) which will also return one of these constants):

| Constant | Cursor |
| --- | --- |
| cr\_none |  |
| cr\_default |  |
| cr\_arrow |  |
| cr\_cross |  |
| cr\_beam |  |
| cr\_size\_nesw |  |
| cr\_size\_ns |  |
| cr\_size\_nwse |  |
| cr\_size\_we |  |
| cr\_uparrow |  |
| cr\_hourglass |  |
| cr\_drag |  |
| cr\_appstart |  |
| cr\_handpoint |  |
| cr\_size\_all |  |

 

#### Syntax:

window\_set\_cursor(cursor)

| Argument | Type | Description |
| --- | --- | --- |
| cursor | Cursor Constant | The cursor to set for the game window. |

 

#### Returns:

N/A

 

#### Example:

if (mouse\_check\_button\_pressed(mb\_left))   

 {  

     window\_set\_cursor(cr\_drag);  

 }

The above code will change the window cursor to the standard windows drag cursor if the left mouse button has been pressed.
