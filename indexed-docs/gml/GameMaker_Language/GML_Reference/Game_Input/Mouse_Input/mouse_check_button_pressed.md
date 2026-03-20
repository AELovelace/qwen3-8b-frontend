# mouse\_check\_button\_pressed

This function will return true if the mouse button being checked has been pressed or false if it has not.

This function will only return true *once* for any mouse button when it is first pressed and in order for it to return true again the button will need to have been released and pressed again. Note that it will be considered pressed for the duration of the step, and for all instances that have any mouse events or that use this same function.

You supply the mouse button to check from one of the following constants:

 
#### Syntax:

mouse\_check\_button\_pressed(numb)

| Argument | Type | Description |
| --- | --- | --- |
| numb | [Mouse Button Constant](../../../../../GameMaker_Language/GML_Reference/Game_Input/Mouse_Input/mouse_check_button.md) | Which mouse button constant to check for. |

 

#### Returns:

[Boolean](../../../../../GameMaker_Language/GML_Overview/Data_Types.md)

 

#### Example:

if mouse\_check\_button\_pressed(mb\_left)  

 {  

     score \+\= 50;  

 }

The above code will check to see if the left mouse button has been pressed and if it has it will add 50 to the score.
