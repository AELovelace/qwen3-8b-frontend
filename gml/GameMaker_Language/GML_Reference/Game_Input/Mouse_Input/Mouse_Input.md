# Mouse Input

Mouse input is accepted on all platforms (on mobile devices it is accepted as a single screen touch \- if you need to use multi\-touch, you should be using the [device\-specific functions](../Device_Input/Device_Input.md)) and has a few constants that are used to specify the buttons being pressed. These constants are shown in the following table:

 
The following functions exist for the standard mouse button controls:

- [mouse\_button](mouse_button.md)
- [mouse\_check\_button](mouse_check_button.md)
- [mouse\_check\_button\_pressed](mouse_check_button_pressed.md)
- [mouse\_check\_button\_released](mouse_check_button_released.md)
- [mouse\_clear](mouse_clear.md)
- [mouse\_lastbutton](mouse_lastbutton.md)
- [mouse\_wheel\_up](mouse_wheel_up.md)
- [mouse\_wheel\_down](mouse_wheel_down.md)
- [mouse\_x](mouse_x.md)
- [mouse\_y](mouse_y.md)

 

There are also a set of window functions related to using the mouse on desktop targets:

- [window\_mouse\_get\_x](../../Cameras_And_Display/The_Game_Window/window_mouse_get_x.md)
- [window\_mouse\_get\_y](../../Cameras_And_Display/The_Game_Window/window_mouse_get_y.md)
- [window\_mouse\_set](../../Cameras_And_Display/The_Game_Window/window_mouse_set.md)
- [window\_view\_mouse\_get\_x](../../Cameras_And_Display/The_Game_Window/window_view_mouse_get_x.md)
- [window\_view\_mouse\_get\_y](../../Cameras_And_Display/The_Game_Window/window_view_mouse_get_y.md)
- [window\_views\_mouse\_get\_x](../../Cameras_And_Display/The_Game_Window/window_views_mouse_get_x.md)
- [window\_views\_mouse\_get\_y](../../Cameras_And_Display/The_Game_Window/window_views_mouse_get_y.md)

## Mouse Coordinates

You can get the coordinates of the mouse within the room using [mouse\_x](mouse_x.md) and [mouse\_y](mouse_y.md). There are also functions for getting the raw or GUI mouse coordinates, please see [Device Input](../Device_Input/Device_Input.md).
