# mouse\_lastbutton

This variable returns the last mouse button that was pressed and can return any of the special [mouse constants](Mouse_Input.md) except mb\_any (you may also set this variable to one of the constants).

 

#### Syntax:

mouse\_lastbutton

 

#### Returns:

[Mouse Button Constant](mouse_check_button.md) (except mb\_any)

 

#### Example:

if (mouse\_lastbutton \=\= mb\_left)  

 {  

     x \-\= 1;  

 }

This code moves the current instance left if the last button pressed was the left mouse button.
