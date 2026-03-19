# mouse\_button

This **read\-only** variable returns the mouse button that is currently being pressed (currently, as in, this step) and can return any of the special [mouse constants](Mouse_Input.md) except mb\_any.

 

#### Syntax:

mouse\_button

 

#### Returns:

[Mouse Button Constant](mouse_check_button.md) (except mb\_any)

 

#### **Example:**

if (mouse\_button \=\= mb\_left)  

 {  

     x \-\= 1;  

 }

This code moves the current instance left if the left mouse button is down.
