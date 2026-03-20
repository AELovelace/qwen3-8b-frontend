# mouse\_check\_button\_released

This function will return true if the mouse button being checked has been released or false if it has not.

This function will only return true *once* for any mouse button when it is released and in order for it to return true again the button will need to have been pressed and released again. Note that it will be considered released for the duration of the step, and for all instances that have any mouse events or that use this same function.

You supply the mouse button to check from one of the following constants:

 
#### Syntax:

mouse\_check\_button\_released(numb)

| Argument | Type | Description |
| --- | --- | --- |
| numb | [Mouse Button Constant](../../../../../GameMaker_Language/GML_Reference/Game_Input/Mouse_Input/mouse_check_button.md) | Which mouse button constant to check for. |

 

#### Returns:

[Boolean](../../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

if mouse\_check\_button\_released(mb\_right)  

 {  

     speed \= point\_distance(x, y, mouse\_x, mouse\_y) / 10;  

 }

The above code will check to see if the right mouse button has been released and if it has it will set the speed of the instance to a tenth of the distance between the current x/y position and the mouse x/y position.
