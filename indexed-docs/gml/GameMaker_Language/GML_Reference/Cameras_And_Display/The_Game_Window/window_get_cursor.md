# window\_get\_cursor

With this function you can get the current cursor being used in the game window, with the return value being any one of the constants listed below (to set the current cursor being used you can use the function [window\_set\_cursor()](../The_Game_Window/window_set_cursor.md) which also takes these constants):

| [Cursor Constant](GameMaker_Language/GML_Reference/Cameras_And_Display/The_Game_Window/window_get_cursor.md) | |
| --- | --- |
| Constant | Cursor |
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

window\_get\_cursor()

 

#### Returns:

[Cursor Constant](GameMaker_Language/GML_Reference/Cameras_And_Display/The_Game_Window/window_get_cursor.md)

 

#### Example:

if (mouse\_check\_button\_pressed(mb\_left))   

 {  

     if (window\_get\_cursor() !\= cr\_drag) window\_set\_cursor(cr\_drag);  

 }

The above code will change the window cursor to the standard windows drag cursor if the left mouse button has been pressed and it has not already been changed previously.
