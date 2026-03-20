# mouse\_check\_button

This function will return true if the mouse button being checked is held down or false if it is not.

You supply the mouse button to check from one of the following constants:

 
#### Syntax:

mouse\_check\_button(numb)

| Argument | Type | Description |
| --- | --- | --- |
| numb | [Mouse Button Constant](mouse_check_button.md) | Which mouse button constant to check for. |

 

#### Returns:

[Boolean](../../../GML_Overview/Data_Types.md)

 

#### Example:

if mouse\_check\_button(mb\_left)  

 {  

     instance\_create\_layer(mouse\_x, mouse\_y, "Effects", obj\_Star);  

 }

The above code will check for the left mouse button and every step that it is held down will create an instance of the object indexed in obj\_Star.
